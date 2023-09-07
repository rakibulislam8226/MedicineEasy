# Pull base image
FROM python:3.10-alpine

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /src

# Install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Install libmagic from the host system to the Docker image
RUN apk add --no-cache file

# Copy project
COPY . .