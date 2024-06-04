# Use a specific version of Python
FROM python:3.11-slim


# Set the working directory in the container
WORKDIR /app/src
COPY ./requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy the current directory contents into the container at /usr/src/app

# Run app.py when the container launches
CMD ["python", "app.py"]
