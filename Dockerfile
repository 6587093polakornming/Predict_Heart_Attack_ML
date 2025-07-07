# Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code into image
COPY . .

EXPOSE 8100

# Run the FastAPI server
CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8100"]