from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

def run_test():
    base_url = os.getenv("BASE_URL", "http://optimy-app:8080")
    
    # Set up Selenium with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(base_url)

        # Check if the page contains the expected content
        body = driver.find_element(By.TAG_NAME, "body")
        assert "id: 1 - Name: Hello Optimy - Year: 2024" in body.text, "Expected text not found"
        print("Test passed: Application is up and running, displaying correct data.")
    except AssertionError as e:
        print(f"Test failed: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    run_test()
