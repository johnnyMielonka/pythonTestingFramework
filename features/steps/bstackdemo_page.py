from behave import *
from src.pages.generic_page import GenericPage
from src.pages.home_page import HomePage
from src.pages.sign_in_page import SignInPage
from src.core.driver_factory import WebdriverFactory

driver = WebdriverFactory.getDriver("chrome")

@given('Open {url} url')
def step_impl(context, url: str) -> None:
    driver.get(url)

@when('Go to login page')
def step_impl(context) -> None:
    homepage : WebdriverFactory = HomePage(driver)
    homepage.click_sign_in()

@when('log in as "{user}" user and "{pswd}" password')
def step_impl(context, user: str, pswd: str) -> None:
    sign_in_page : WebdriverFactory = SignInPage(driver)
    sign_in_page.select_username(user)
    sign_in_page.select_password(pswd)
    sign_in_page.click_login()

@then('Verify if page title is {expected_title}')
def step_impl(context, expected_title: str) -> None:
    generic_page : WebdriverFactory = GenericPage(driver)
    print (generic_page.get_page_title())
    assert generic_page.get_page_title() == expected_title
