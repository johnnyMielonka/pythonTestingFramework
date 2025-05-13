from seleniumpagefactory.Pagefactory import PageFactory

class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'user_name': ('CSS', "#username input"),
    'password': ('CSS', '#password input'),
    'login_btn': ('ID', 'login-btn')
    }

    def select_username(self, user: str) -> None:
        self.user_name.set_text(f'{user}\n')

    def select_password(self, password: str) -> None:
        self.password.set_text(f'{password}\n')

    def click_login(self) -> None:
        self.login_btn.click()