#FROM selenium/standalone-chrome

FROM python:3.11-slim
# Set the working directory
WORKDIR /app

# Switch to root user to install dependencies
USER root

# Install Python and related dependencies
RUN apt-get update && apt-get install -y python3 python3-distutils wget

# Install pip
# RUN wget https://bootstrap.pypa.io/get-pip.py
# RUN python3 get-pip.py

# Install Python packages including selenium
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY ./src/ /app/src/

# Verify installations (optional, you can remove these lines if not needed)
#RUN google-chrome --version
#RUN chromedriver --version

# Set the display number for xvfb (uncomment if needed)
# ENV DISPLAY=:99
# Run the main Python script
WORKDIR /app/src

CMD ["python3", "source_data.py"]