from selenium.webdriver.common.by import By
import time
import os

def wait_and_act(driver, xpath, action="click", value=None, timeout=20, interval=0.5):
    """
    Waits for an element to be available, then performs an action on it.

    Parameters:
        driver  : WebDriver instance.
        xpath   : XPath of the element.
        action  : Action to perform ('click', 'send_keys', 'get').
        value   : Value to send (only used when action is 'send_keys').
        timeout : Maximum wait time in seconds.
        interval: Time between retries in seconds.

    Returns:
        WebElement if action is 'get', else None.
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            element = driver.find_element(By.XPATH, xpath)
            if action == "click":
                element.click()
                print(f"Clicked element: {xpath}")
            elif action == "send_keys":
                element.send_keys(value)
                print(f"Entered '{value}' into element: {xpath}")
            return None
        except:
            print(f"Waiting for element: {xpath}...")
            time.sleep(interval)
    print(f"Timeout: Element not found - {xpath}")
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