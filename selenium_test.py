from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up headless Chrome browser
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Run without UI
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Open YouTube
    driver.get("https://www.youtube.com")
    time.sleep(2)

    # Find search box and search for "ChatOps"
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys("ChatOps")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)  # Wait for results to load

    # Check if results are loaded
    results = driver.find_elements(By.ID, "video-title")
    if results:
        print("Test Passed: Search results loaded successfully!")
    else:
        print("Test Failed: No results found!")

except Exception as e:
    print(f"Test Error: {e}")

finally:
    driver.quit()  # Close the browser
