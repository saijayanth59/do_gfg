from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from constants import GFG_xpath as GFG
from utils import wait_and_act, get_gfg_credentials
from time import sleep


def login_gfg(driver):
    gmail, password = get_gfg_credentials()

    print("Opening GeeksforGeeks...")
    driver.get(GFG["pod_link"])

    wait_and_act(driver, GFG["signin_btn"])

    wait_and_act(driver, GFG["gmail"], action="send_keys", value=gmail)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    wait_and_act(driver, GFG["password"], action="send_keys", value=password)

    wait_and_act(driver, GFG["login_btn"])

    print("Login attempt completed.")

    sleep(3)
    
    driver.get(wait_and_act(driver, GFG["pod_solve_btn"], action="get").get_attribute("href"))



    url = "https://codeshare.io/do_gfg"
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(url)

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)
    actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)
    actions.perform()
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

    print(f"Opened new tab: {url}")
    select_python3(driver)
    send_backspace(driver)
    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    actions.key_down(Keys.CONTROL).send_keys(Keys.ENTER).key_up(Keys.CONTROL)
    actions.perform()


def select_python3(driver):
    wait_and_act(driver=driver, locator_type=By.CLASS_NAME, locator="ui.selection.dropdown")

    wait_and_act(driver=driver, locator="//div[@role='option']//span[text()='Python3']")
    print("Python3 selected successfully.")

def send_backspace(driver, limit=100):
    """
    Sends Backspace keypress globally from the current cursor position.

    Parameters:
        driver  : WebDriver instance.
        limit   : Number of times to press Backspace.
        interval: Delay between key presses (default: 0.1s).
    """
    actions = ActionChains(driver)
    for _ in range(limit):
        actions.send_keys(Keys.BACKSPACE).perform()
