# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /usr/src/app

# Install required packages
RUN apt-get update && \
    apt-get install -y wget unzip curl gnupg --no-install-recommends && \
    apt-get install -y libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 libnss3 libxrandr2 libasound2 libpango1.0-0 libpangocairo-1.0-0 libatk1.0-0 libatk-bridge2.0-0 libgtk-3-0 libdrm2 libgbm1 libnspr4 libxss1 libxrandr2 xdg-utils && \
    rm -rf /var/lib/apt/lists/*

# Install Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Install Selenium and WebDriver Manager
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Selenium script
COPY selenium_test.py ./

# Command to run the Selenium script
CMD ["python", "selenium_test.py"]
