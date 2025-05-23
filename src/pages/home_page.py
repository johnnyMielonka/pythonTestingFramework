from seleniumpagefactory.Pagefactory import PageFactory

class HomePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    "sign_in": ("ID", "signin"),
    "user_name": ("CSS", ".username")
    }

    def click_sign_in(self) -> None:
        self.sign_in.click()

    def get_username(self) -> None:
        retrieved_username = self.user_name.get_text()
        assert retrieved_username == "demouser"
