FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ src/
# COPY smoke_test.py .

# Copy tests if needed for internal test running, but usually not needed for prod image
# COPY tests/ tests/

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
