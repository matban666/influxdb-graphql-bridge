# Use a lightweight Python image as the base
FROM python:3.11-slim

# Set a working directory for the application
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy project code (replace 'myproject' with your project name)
COPY . .

# Expose the port where Django runs (usually 8000)
EXPOSE 8000

# Set the command to run when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]