import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class FluentWait:
    DEFAULT_TIMEOUT = 10
    DEFAULT_POLL_FREQ = 0.5

    @staticmethod
    def for_visibility(driver, element, timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(driver, timeout, poll_frequency)
        return wait.until(EC.visibility_of(element))

    @staticmethod
    def for_title_contains(driver, title, timeout=10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.title_contains(title))

    @staticmethod
    def for_title_is(driver, expected_title, timeout=10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.title_is(expected_title))

    @staticmethod
    def for_url_contains(driver, url, timeout=10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.url_contains(url))

    @staticmethod
    def for_element_present(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @staticmethod
    def wait_for(condition_func, driver, timeout=10, poll_frequency=0.5):
        wait = WebDriverWait(driver, timeout, poll_frequency)
        return wait.until(condition_func)


class Retry:
    @staticmethod
    def retry_on_exception(func, retries=3, delay=1, exceptions=(Exception,)):
        for attempt in range(retries):
            try:
                return func()
            except exceptions as e:
                if attempt == retries - 1:
                    raise
                time.sleep(delay)


def close_driver(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if hasattr(func, 'driver'):
            func.driver.close()
        return result
    return wrapper


def get_webelement_by_text(driver, xpath, *text):
    xpath = xpath % text
    return driver.find_element(By.XPATH, xpath)