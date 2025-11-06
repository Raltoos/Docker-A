# backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Use gunicorn in container for production-like serving
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
