import time
from behave import *
from src.pages.generic_page import GenericPage
from src.pages.home_page import HomePage
from src.pages.sign_in_page import SignInPage
from src.core.driver_factory import WebdriverFactory
from src.core.helpers import FluentWait

@when('Go to login page')
def step_impl(context) -> None:
    homepage : WebdriverFactory = HomePage(context.driver)
    homepage.click_sign_in()

@when('log in as "{user}" user and "{pswd}" password')
def step_impl(context, user: str, pswd: str) -> None:
    sign_in_page : WebdriverFactory = SignInPage(context.driver)
    sign_in_page.select_username(user)
    sign_in_page.select_password(pswd)
    sign_in_page.click_login()

@then('Verify if page title is {expected_title}')
def step_impl(context, expected_title: str) -> None:
    driver = context.driver
    loading_titles = ["Cierpliwości", "Proszę czekać", "Loading", " Ładowanie"]
    
    for _ in range(15):
        actual_title = driver.title
        if actual_title not in loading_titles:
            break
        time.sleep(1)
    
    actual_title = driver.title
    print(f"Actual title: {actual_title}")
    assert expected_title in actual_title or actual_title in expected_title, \
        f"Expected title containing '{expected_title}', but got '{actual_title}'"
