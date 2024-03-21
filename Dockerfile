# Using official python image
FROM python:3.10-slim

# Set working directory in the container to /app
WORKDIR /app

# Copy only the important files
COPY src/ src/
COPY test/ test/
COPY pyproject.toml requirements.txt ./

# Install packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the application
CMD ["pytest", "test/test_MatrixMult.py"]
