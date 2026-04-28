import os
import time
from behave import *
from src.pages.generic_page import GenericPage
from src.core.driver_factory import WebdriverFactory

def apply_slow_motion():
    slow_motion = os.environ.get("SLOW_MOTION")
    if slow_motion:
        time.sleep(float(slow_motion))

@given('demo123')
def step_impl(context) -> None:
    print('demo')

@given(u'Open "{url}" url')
def step_impl(context, url: str) -> None:
    context.driver.get(url)
    apply_slow_motion()

@given('Start new "{browser}" browser')
def step_impl(context, browser):
    if not hasattr(context, 'driver'):
        context.driver = WebdriverFactory.getDriver(browser)
