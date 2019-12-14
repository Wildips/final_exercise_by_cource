from .pages.main_page import MainPage
from .pages.product_page import ProductPage#, BasketPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()

    p_page = ProductPage(browser, link)
#    page.open()
    p_page.should_be_button_add_to_basket()
    p_page.should_be_product_link_xmass()
    p_page.should_be_book_name()
    p_page.should_be_book_price()
    p_page.should_be_basket_price()
    p_page.should_be_to_basket_link()
    book_name_on_product_page = str(p_page.get_book_name())
    book_price_on_product_page = str(p_page.get_book_price())

    #click__button
    p_page.click_on_add_to_basket_btn()

    #promt window
#    p_page.accept_promt_window_after_book_was_added()

    #time.sleep(60)

#    p_page.accept_congratulations_alert()

    p_page.solve_quiz_and_get_code()

    time.sleep(5)

    p_page.should_be_adding_result_book_name()
    p_page.should_be_adding_result_basket_price()

    #price correct
    assert book_price_on_product_page != str(p_page.get_basket_book_price()),"Book price on page : "+book_price_on_product_page+" not correspond basket price : "+str(p_page.get_basket_book_price())

    #new basket price after click
    #assert book_price_on_product_page != str(p_page.get_adding_result_basket_price()),"Book price on page : "+book_price_on_product_page+" not correspond after click price : "+str(p_page.get_adding_result_basket_price())

    #new basket book name correspont before name
    #assert book_name_on_product_page != str(p_page.get_adding_result_book_name()),"Book price on page : "+book_name_on_product_page+" not correspond after click price : "+str(p_page.get_adding_result_book_name())

    #go into basket link
#    p_page.click_on_link_to_basket()

    #book in basket
#    bas_page = BasketPage(browser, link)
#    bas_page.should_be_in_basket_link()
#    bas_page.shold_be_basket_book_name()

    #book name_from_basket correct
#    assert book_price_on_product_page != str(bas_page.get_in_basket_book_name()),"Book name on page : "+book_price_on_product_page+" not correspond basket name : "+str(bas_page.get_in_basket_book_name())

