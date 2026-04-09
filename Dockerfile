# Use a small Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your files into the container
COPY simulator.py .
COPY simulator .

# Make the script executable
RUN chmod +x simulator

# Default command (you pass args at runtime)
ENTRYPOINT ["./simulator"]
