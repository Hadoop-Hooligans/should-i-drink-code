provider "aws" {
  region = var.region
}

resource "aws_instance" "DATA472-jre141-hdg-controller" {
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
    host        = aws_instance.DATA472-jre141-hdg-controller.public_ip
    private_key = file("${var.wsl_path}//${var.instance_keypair_name}.pem")
  }
  provisioner "remote-exec" {
    inline = [
      "echo 'AWS EC2 CONTROLLER ${var.instance_type}'",
      "echo 'Initial configuration ${timestamp()}'",
      "sudo apt update",
      "sudo apt install -y git dos2unix",
      "sudo rm -rf  ${var.git_repo_dir}",
      "git clone -b ${var.git_branch} ${var.git_repo} ${var.git_repo_dir}",
      "cd ${var.git_repo_dir}",
      "mkdir -p logs",
      "dos2unix $(find . -name '*.sh' -type f)",
      "sh ./scripts/setup-controller.sh"
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
    host        = aws_instance.DATA472-jre141-hdg-controller.public_ip
    private_key = file("${var.wsl_path}//${var.instance_keypair_name}.pem")
  }

  provisioner "remote-exec" {
    inline = [
      "echo 'AWS EC2 CONTROLLER ${var.instance_type}'",
      "echo 'starting scraper ${timestamp()}'",
      "cd /home/ubuntu/${var.git_repo_dir}",
      "sh ./scripts/controller-main.sh",
	  "echo '0 2 * * 2 /home/ubuntu/should-i-drink-code/scripts/docker_cron_tab.sh' > crontab",
	  "crontab -l crontab"
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
    host        = aws_instance.DATA472-jre141-hdg-controller.public_ip
    private_key = file("${var.wsl_path}/${var.instance_keypair_name}.pem")
  }

  # Use the file provisioner to copy a file from local machine to remote server
  provisioner "file" {
    source      = "../../../../.env"  # Path to the local file
    destination = "/home/ubuntu/.env" # Destination path on the remote server
  }
}

output "ec2_global_ips" {
  value = aws_instance.DATA472-jre141-hdg-controller.*.public_ip
}

output "ec2_instance_finished" {
  value = "Done \n please set up .env under ${var.git_repo_dir} and then run the database script"
}