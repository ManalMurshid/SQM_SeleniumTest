# Selenium Login Automation

## Overview
This project automates the login functionality for the sample website (https://opensource-demo.orangehrmlive.com/web/index.php/auth/login) using Selenium WebDriver. 
It tests both valid and invalid login scenarios and verifies the login status.

## Prerequisites
Before running the script, ensure the following are installed:

1. **Python** (version 3.x) - Download from [python.org](https://www.python.org/).
2. **Conda** (Optional, for virtual environment management) - Download from [Anaconda](https://www.anaconda.com/).
3. **Selenium WebDriver & WebDriver Manager** - Install using:
   ```bash
   pip install selenium webdriver-manager
   ```
4. **Web Browser** - Google Chrome (recommended).
5. **WebDriver for your Browser:**
   - The WebDriver Manager package will handle downloading and setting up the required driver automatically.

## Installation & Setup
### 1. Create and Activate a Conda Environment (Optional but Recommended)
```bash
conda create --name selenium_env python=3.9 -y
conda activate selenium_env
```

### 2. Ensure Selenium and WebDriver Manager are Installed
```bash
pip install selenium webdriver-manager
```

### 3. Download or Clone and Access the Project from GitHub
-Clone the repository using the following command:
```bash
git clone <https://github.com/ManalMurshid/SQM_SeleniumTest.git>
```

-Clone the repository using the following command:
```bash
cd <repository folder>
```

  

## Running the Script
1. Open a terminal or command prompt.
2. Navigate to the project directory:
   ```bash
   cd <path_to_project>
   ```
3. Run the script:
   ```bash
   python login_test.py
   ```

## Test Case Scenarios
### Test Case 1: Valid Login
- **Input:** Correct username and password.
- **Expected Output:** "Login Successful" appears.

  

### Test Case 2: Invalid Login
- **Input:** Incorrect username or password.
- **Expected Output:** "Login Failed" appears.

### Test Case 3: Empty Credentials
- **Input:** Leave username and password fields blank.
- **Expected Output:** Error message prompts the user to enter credentials.

## Notes
- Ensure the correct WebDriver is used for your browser version.
- Modify the script as needed to test different credentials.
- If encountering issues, check for WebDriver version mismatches or incorrect element locators.

## Additional Resources
- Selenium Documentation: [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
- WebDriver Downloads: [https://www.selenium.dev/downloads/](https://www.selenium.dev/downloads/)

