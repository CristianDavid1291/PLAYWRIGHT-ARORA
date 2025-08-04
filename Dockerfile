FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies required for Playwright
RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libxcb-dri3-0 \
    libxdamage1 \
    libxfixes3 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers (using Chromium only for minimal test execution)
RUN playwright install --with-deps chromium

# Copy project files
COPY . .

# Set environment variable for module resolution
ENV PYTHONPATH=/app

# Default command to run tests using pytest in headless mode
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q", "--browser", "chromium"]