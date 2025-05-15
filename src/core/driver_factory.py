from selenium import webdriver

class WebdriverFactory():
    @staticmethod
    def getDriver(browser: str) -> webdriver:
        match browser:
            case "chrome":
                chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_argument("start-maximized")
                driver = webdriver.Chrome(options=chrome_options)
            case "safari":
                safari_options = webdriver.SafariOptions()
                # safari_options.add_argument("start-maximized")
                driver = webdriver.Safari(options=safari_options)
            case _:
                raise ValueError(f'Unknown browser name {browser}')
        print(f"{browser} driver started")
        return driver

if __name__ == "__main__":
    WebdriverFactory.getDriver("safari")