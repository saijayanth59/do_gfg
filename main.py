from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from agents.x import login_x


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    login_x(driver)
    while True:
        pass


