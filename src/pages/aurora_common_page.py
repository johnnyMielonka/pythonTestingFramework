from seleniumpagefactory.Pagefactory import PageFactory
from selenium.webdriver.common.by import By
from src.core import helpers

class AuroraCommon(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    generic_menubar_item: str = "//div[@class='template_nav_main']//a[@class='navitem' and text()='%s']"
    menubar_items: str = "//div[@class='template_nav_main']//a[@class='navitem']"

    def click_menubar_item(self, item) -> None:
        xpath: str = self.generic_menubar_item % item
        self.driver, helpers.get_webelement_by_text(self.driver, xpath, item).click()
        # self.driver.find_element(By.XPATH, xpath).click()
    
    def get_menubar_items(self) -> list[str]:
        return list(map(lambda x: x.get_text(), self.driver.find_elements(By.XPATH, self.menubar_items)))


    def get_username(self) -> None:
        retrieved_username = self.user_name.get_text()
        assert retrieved_username == "demouser"

    def get_web_element(self, xpath, *text):
        return super().get_web_element(*loc)