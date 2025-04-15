# Use the official Python image
FROM python:3.11-slim

COPY requirements.txt /src/requirements.txt
WORKDIR /src/
RUN pip install --no-cache-dir --force-reinstall  -r requirements.txt
# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*
COPY . /src

EXPOSE 5000
ENTRYPOINT ["gunicorn","run:app","-w","4", "--bind", "0.0.0.0:5000"]
