import pytest

from .pages.main_page import MainPage
from .pages.product_page import ProductPage#, BasketPage
import time

#after buged link was found and msrked list
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])


#product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]
#@pytest.mark.parametrize('link', urls)


def test_guest_can_add_product_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()

    p_page = ProductPage(browser, link)
    p_page.should_be_button_add_to_basket()

    #prepare postfix
    link_postfix=link[link.find('/?')+len(('/?')):]

    p_page.should_be_product_link_xmass(link_postfix)
    p_page.should_be_lang_select_button()
    p_page.should_be_book_name()
    p_page.should_be_book_price()
    p_page.should_be_basket_price()
    p_page.should_be_to_basket_link()
    p_page.should_be_present_search_button()
    p_page.should_be_language_preseted()
    book_name_on_product_page = str(p_page.get_book_name())
    book_price_on_product_page = str(p_page.get_book_price())

    #click__button
    p_page.click_on_add_to_basket_btn()

    #promt window
    p_page.solve_quiz_and_get_code()

    time.sleep(3)

    #price correct
    p_page.compare_book_price_with_top_basket_price(book_price_on_product_page)

    #compare ordered book name with after ckicking result
    p_page.find_ordered_book_name_in_after_click_changes(book_name_on_product_page)

    #new basket price after click
    p_page.find_ordered_book_price_in_after_click_changes(book_price_on_product_page)

