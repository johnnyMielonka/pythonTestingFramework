import sys
sys.path.append(sys.path[0] + "/..")

from src.pages.home_page import HomePage
from src.pages.sign_in_page import SignInPage
from src.core.driver_factory import WebdriverFactory

def test_browserstack(browser: str):
    driver = WebdriverFactory.getDriver(browser)
    driver.get("https://bstackdemo.com/")

    homepage = HomePage(driver)
    sign_in_page = SignInPage(driver)

    homepage.click_sign_in()
    sign_in_page.select_username("test")
    sign_in_page.select_password("aaa")
    sign_in_page.click_login()
    print(f"PASS!!\n")

    driver.quit()

if __name__ == "__main__":
    browsers: list=("chrome", "safari", "error")
    for browser in browsers:
        test_browserstack(browser)