# Use a lightweight Python base image
FROM python:3.10-slim

# Install system dependencies (Tesseract + PDF tools)
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    poppler-utils \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY goodle_core.py /app/
COPY goodle_app.py /app/
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download required NLTK data
RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader punkt_tab
RUN python3 -m nltk.downloader stopwords

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit UI
CMD ["streamlit", "run", "goodle_app.py", "--server.port=8501", "--server.address=0.0.0.0"]

