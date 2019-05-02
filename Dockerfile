# Use an official Python runtime as a parent image
FROM python:3.7.2-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install all dependencies
RUN python setup.py develop 

# Expose port
EXPOSE 6543

WORKDIR /app