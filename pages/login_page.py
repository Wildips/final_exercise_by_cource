from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        #assert "login" not in str(self.browser.current_url), "Login link is not found 'login' : "+str(self.browser.current_url)
        assert self.is_element_present(*LoginPageLocators.LOGIN_URL), "Login link is not presented : "+str(self.browser.current_url)

        # реализуйте проверку на корректный url адрес
        #assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма логина
        #assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login form is not presented"
        # реализуйте проверку, что есть форма регистрации на странице
        #assert True
