from selenium.webdriver.common.by import By
import time
import os

def wait_and_act(driver, locator, locator_type=By.XPATH, action="click", value=None, timeout=20, interval=0.5):
    """
    Waits for an element to be available, then performs an action on it.

    Parameters:
        driver       : WebDriver instance.
        locator      : Locator string (XPath, Class Name, etc.).
        locator_type : Type of locator (By.XPATH, By.CLASS_NAME, etc.).
        action       : Action to perform ('click', 'send_keys', 'get').
        value        : Value to send (only used when action is 'send_keys').
        timeout      : Maximum wait time in seconds.
        interval     : Time between retries in seconds.

    Returns:
        WebElement if action is 'get', else None.
    """
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        try:
            element = driver.find_element(locator_type, locator)

            if action == "click":
                element.click()
                print(f"Clicked element: {locator}")
            elif action == "send_keys":
                element.send_keys(value)
                print(f"Entered '{value}' into element: {locator}")
            elif action == "get":
                return element
            
            return None 

        except:
            print(f"Waiting for element: {locator}...")
            time.sleep(interval)

    print(f"Timeout: Element not found - {locator}")
    return None



def get_X_credentials():
    """
    Retrieves X credentials from environment variables.

    Returns:
        Tuple containing Gmail, Username, and Password.
    """
    gmail = os.environ.get("X_GMAIL", "")
    username = os.environ.get("X_USERNAME", "")
    password = os.environ.get("X_PASSWORD", "")
    return gmail, username, password


def get_gfg_credentials():
    gmail = os.environ.get("GFG_GMAIL", "")
    password = os.environ.get("GFG_PASSWORD", "")
    return gmail, password
