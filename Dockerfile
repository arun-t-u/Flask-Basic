# Use the official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /src/

# Copy requirements
COPY requirements.txt /src/requirements.txt

# Install system dependencies required by mysqlclient and others
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code
COPY . /src

# Expose the app port
EXPOSE 5000

# Start the app with Gunicorn
ENTRYPOINT ["gunicorn","run:app","-w","4", "--bind", "0.0.0.0:5000"]
