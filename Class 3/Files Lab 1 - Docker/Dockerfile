# Use an official Python runtime as a parent image, this is the base image to build the enviroment my code will run on.
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

#                                                 [The command, parameter 1]
# Run the script when the container launches, CMD ["python", "app.py"] specifies that when the container starts, it should run python app.py.
CMD ["python", "/app/script.py"]
