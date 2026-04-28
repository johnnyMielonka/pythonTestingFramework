import os
from selenium import webdriver

class WebdriverFactory():
    @staticmethod
    def getDriver(browser: str) -> webdriver:
        headless = os.environ.get("HEADLESS", "true").lower() == "true"
        
        match browser:
            case "chrome":
                chrome_options = webdriver.ChromeOptions()
                if headless:
                    chrome_options.add_argument("--headless")
                chrome_options.add_argument("--no-sandbox")
                chrome_options.add_argument("--disable-dev-shm-usage")
                chrome_options.add_argument("--window-size=1920,1080")
                driver = webdriver.Chrome(options=chrome_options)
            case "safari":
                safari_options = webdriver.SafariOptions()
                driver = webdriver.Safari(options=safari_options)
            case _:
                raise ValueError(f'Unknown browser name {browser}')
        
        driver.implicitly_wait(10)
        print(f"{browser} driver started (headless={headless})")
        return driver

if __name__ == "__main__":
    WebdriverFactory.getDriver("safari")