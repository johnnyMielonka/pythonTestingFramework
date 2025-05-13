from seleniumpagefactory.Pagefactory import PageFactory

class GenericPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self) -> str:
        return self.driver.title