FROM python:3.11-slim

# Environment
ENV PYTHONUNBUFFERED=1 \
    PORT=8501

WORKDIR /app

# Install pip requirements
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy app source
COPY . .

EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
