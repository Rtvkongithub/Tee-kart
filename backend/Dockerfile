# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Run with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
