provider "aws" {
  region = var.region
}

resource "aws_instance" "DATA472-jre141-hdg-terraform-testserver" {
  ami                         = var.ami
  instance_type               = var.instance_type
  subnet_id                   = var.subnetid
  vpc_security_group_ids      = var.vpc_security_group_ids
  associate_public_ip_address = true
  key_name                    = var.instance_keypair_name
  ebs_optimized               = false
  tags = {
    Name     = var.name
    Course   = var.course
    UserName = var.username
  }
  ebs_block_device {
    device_name = "/dev/sda1"
    volume_size = var.volumesize
  }
  volume_tags = {
    Name     = var.name
    Course   = var.course
    UserName = var.username
  }


}
# you will need to put your private_key path.

resource "null_resource" "build_git_repo" {
  connection {
    type        = "ssh"
    user        = var.ssh_user
    host        = aws_instance.DATA472-jre141-hdg-terraform-testserver.public_ip
    private_key = file("//mnt//c//Users//jacob//Downloads//${var.instance_keypair_name}.pem")
  }
  provisioner "remote-exec" {
    inline = [
      "echo 'AWS EC2 CONTROLLER ${var.instance_type}'",
      "echo 'Initial configuration ${timestamp()}'",
      "sudo apt update",
      "sudo apt install -y git",
      "sudo rm -rf  ${var.git_repo_dir}",
      "git clone -b ${var.git_branch} ${var.git_repo} ${var.git_repo_dir}",
      "cd ${var.git_repo_dir} && git pull origin ${var.git_branch}",
      "cd /home/ubuntu/${var.git_repo_dir}",
      "mkdir -p logs"
    ]
  }
}

resource "time_sleep" "wait_10_seconds" {
  depends_on = [null_resource.build_git_repo]

  create_duration = "10s"
}

resource "null_resource" "resume_configuration" {
  depends_on = [null_resource.copy_file]
  connection {
    type        = "ssh"
    user        = var.ssh_user
    host        = aws_instance.DATA472-jre141-hdg-terraform-testserver.public_ip
    private_key = file("//mnt//c//Users//jacob//Downloads//${var.instance_keypair_name}.pem")
  }

  provisioner "remote-exec" {
    inline = [
      "echo 'AWS EC2 CONTROLLER ${var.instance_type}'",
      "echo 'installing aws client and sam only ${timestamp()}'",
      "cd ${var.linux_home}",
      "sudo apt-get update && sudo apt-get install curl unzip zip wget -y",
      "wget https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -O awscliv2.zip",
      "unzip awscliv2.zip",
      "sudo ./aws/install",
      "wget https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip -O aws-sam-cli-linux-x86_64.zip",
      "unzip aws-sam-cli-linux-x86_64.zip -d sam-installation",
      "sudo ./sam-installation/install",
      "echo 'installing terraform only ${timestamp()}'",
      "sudo apt-get update && sudo apt-get install -y gnupg software-properties-common",
      <<-EOF
      wget -O- https://apt.releases.hashicorp.com/gpg | \
      gpg --dearmor | \
      sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null
      EOF
      ,
      <<-EOF
      gpg --no-default-keyring \
          --keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
          --fingerprint
      EOF
      ,
      <<-EOF
      echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
      https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
      sudo tee /etc/apt/sources.list.d/hashicorp.list
      EOF
      ,
      "sudo apt update",
      "sudo apt-get install terraform"
    ]
  }
}

resource "null_resource" "copy_file" {
  # Ensure this resource depends on any necessary resources before copying the file
  depends_on = [time_sleep.wait_10_seconds]

  # Define the connection details for SSH
  connection {
    type        = "ssh"
    user        = var.ssh_user
    host        = aws_instance.DATA472-jre141-hdg-terraform-testserver.public_ip
    private_key = file("${var.wsl_path}/${var.instance_keypair_name}.pem")
  }

  # Use the file provisioner to copy a file from local machine to remote server
  provisioner "file" {
    source      = "../../../../.env"       # Path to the local file
    destination = "${var.linux_home}/.env" # Destination path on the remote server
  }

  provisioner "file" {
    source      = "${var.wsl_path}/${var.instance_keypair_name}.pem"
    destination = "${var.linux_home}/${var.instance_keypair_name}.pem"

  }
}

output "ec2_global_ips" {
  value = aws_instance.DATA472-jre141-hdg-terraform-testserver.*.public_ip
}

output "ec2_instance_finished" {
  value = "Done \n please set up .env under ${var.git_repo_dir} and then run the database script"
}