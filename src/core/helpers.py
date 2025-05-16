from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@staticmethod
def close_driver(func) -> None:
    def wrapper():
        func()
        func.driver.close()
    return wrapper

def get_webelement_by_text(driver, xpath, *text) -> WebElement:
    xpath: str = xpath % text
    return driver.find_element(By.XPATH, xpath)
