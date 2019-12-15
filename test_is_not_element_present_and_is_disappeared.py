import pytest

from pages.main_page import MainPage
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()

    p_page = ProductPage(browser, link)
    p_page.should_be_button_add_to_basket()
    #click__button
    p_page.click_on_add_to_basket_btn()

    #promt window
#    p_page.solve_quiz_and_get_code()

    #check that mes not present
    p_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, link)
    page.open()

    p_page = ProductPage(browser, link)
    # check that mes not present
    p_page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, link)
    page.open()

    p_page = ProductPage(browser, link)
    p_page.should_be_button_add_to_basket()
    #click__button
    p_page.click_on_add_to_basket_btn()

    #promt window
 #   p_page.solve_quiz_and_get_code()

    #check that mes not present
    p_page.should_not_be_after_waited_time_success_message()


