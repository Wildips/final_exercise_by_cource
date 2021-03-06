from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time


#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
#    page = MainPage(browser, link)
#    page.open()

#    page.go_to_login_page()
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

#temporary comment
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    time.sleep(1)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.have_no_goods()
    basket_page.get_message_about_empty()





#@pytest.mark.login_guest
#class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
#    def test_guest_can_go_to_login_page(self, browser):
         # реализация теста

#    def test_guest_should_see_login_link(self, browser):
         # реализация теста
