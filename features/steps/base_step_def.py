from behave import *
from src.pages.generic_page import GenericPage
from src.core.driver_factory import WebdriverFactory

@given('demo123')
def step_impl(context) -> None:
    print('demo')

@given('Open "{url}" url')
def step_impl(context, url: str) -> None:
    context.driver.get(url)

@given('Start new "{browser}" browser')
def step_impl(context, browser):
    if not hasattr(context, 'driver'):
        context.driver = WebdriverFactory.getDriver(browser)
