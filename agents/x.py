from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from constants import X_xpath as X
from utils import wait_and_act, get_X_credentials


def login_x(driver):
    gmail, username, password = get_X_credentials()
    print("Opening X.com...")
    driver.get(X["login_link"])

    wait_and_act(driver, X["signin_btn"])

    wait_and_act(driver, X["gmail"],
                 action="send_keys", value=gmail)

    ActionChains(driver).send_keys(Keys.ENTER).perform()

    wait_and_act(driver, X["username"], action="send_keys", value=username)
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    wait_and_act(driver, X["password"],
                 action="send_keys", value=password)

    wait_and_act(driver, X["login_btn"])

    print("Login attempt completed.")
