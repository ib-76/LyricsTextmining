FROM ubuntu:latest
LABEL authors="iborg"
# Use the correct Python base image
FROM python:3.12-bullseye

# Set working directory
WORKDIR /app

# Copy dependency list first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your script(s) into the image
COPY Scraper.py .

# Create a SimilarityData directory (inside the app folder for clarity)
RUN mkdir -p /app/Songs

# Run the scraper by default
CMD ["python", "Scraper.py"]
