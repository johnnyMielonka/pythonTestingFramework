from behave import *
from time import sleep
from src.pages.aurora_common_page import AuroraCommon
from src.core.driver_factory import WebdriverFactory

@when(u'Click on menu item')
def step_impl(context) -> None:
    aurora_common : WebdriverFactory = AuroraCommon(context.driver)

    for item in context.table:
        aurora_common.click_menubar_item(item['item'])
        sleep(2)

@then('Verify if following menu bar items are available')
def step_impl(context) -> None:
    aurora_common : WebdriverFactory = AuroraCommon(context.driver)
    expected_elements: list[str] = list(map(lambda x: x['item'], context.table))
    print(expected_elements)
    print(aurora_common.get_menubar_items())
    assert (expected_elements.sort() == aurora_common.get_menubar_items().sort())