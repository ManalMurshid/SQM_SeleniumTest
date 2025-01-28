from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login(username, password):
    # Set up the WebDriver (Make sure you have chromedriver installed)
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    
    time.sleep(3)  # Wait for the page to load
    
    # Locate username and password fields
    username_field = driver.find_element(By.NAME, "username")
    password_field = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[contains(@class, 'oxd-button')]" )
    
    # Enter login credentials
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    # Click the login button
    login_button.click()
    
    time.sleep(5)  # Wait for login process
    
    try:
        # Check if login was successful by looking for an element that appears upon login
        driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        print("Login Successful")
    except:
        print("Login Failed")
    
    # Close the browser
    driver.quit()

if __name__ == "__main__":
    print("Testing valid login...")
    test_login("Admin", "admin123")
    
    print("Testing invalid login...")
    test_login("wronguser", "wrongpassword")
