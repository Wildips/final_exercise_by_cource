import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage#, solve_quiz_and_get_code
from .locators import ProductPageLocators#, ProductBasketIn



class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.should_be_product_link_xmass()
        self.should_be_book_name()
        self.should_be_book_price()
        self.should_be_basket_price()
        self.should_be_to_basket_link()
        self.click_on_add_to_basket_btn()
        self.click_on_link_to_basket()
        self.accept_promt_window_after_book_was_added()
        self.get_book_name()
        self.get_basket_book_price()
        self.get_book_price()

    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.TO_BASKET_BTN), "To basket button is absent."

    def should_be_product_link_xmass(self):
        #assert self.is_element_present(*ProductPageLocators.MARY_LINK), "Wrong url - wrong page."
        #"+(str(self.browser.current_url.find(u"promo=newYear")))+"
        assert u"promo=newYear" in str(self.browser.current_url), "Login link is not found 'login' : "+str(self.browser.current_url)
        #assert self.is_element_present(*ProductPageLocators.MARY_LINK), "Wrong url - wrong page : "+self.is_element_present(*ProductPageLocators.MARY_LINK)

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is absent."

    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is absent."

    def should_be_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Book price is absent."

    def should_be_to_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.GO_TO_BASKET), "Link into basket is absent."

    def click_on_add_to_basket_btn(self):
        button = self.browser.find_element(*ProductPageLocators.TO_BASKET_BTN)
        button.click()

    def click_on_link_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.TO_BASKET_BTN)
        link.click()

    def get_book_name(self):
        x_element = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return x_element.text

    def get_basket_book_price(self):
        x_element = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        return x_element.text

    def get_book_price(self):
        x_element = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return x_element.text

    def accept_promt_window_after_book_was_added(self):
        #answer=solve_quiz_and_get_code(self)
        prompt = self.browser.switch_to.alert
        #prompt.send_keys(str(answer))
        prompt.accept()

    def accept_congratulations_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



    def should_be_adding_result_book_name(self):
        assert self.is_element_present(*ProductPageLocators.AFTER_ADDING_BOOK_NAME), "new book name is absent."

    def should_be_adding_result_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.AFTER_ADDING_BASKET_PRICE), "nwe book price is absent."

    def get_adding_result_book_name(self):
        x_element = self.browser.find_element(*ProductPageLocators.AFTER_ADDING_BOOK_NAME)
        return x_element.text


    def get_adding_result_basket_price(self):
        x_element = self.browser.find_element(*ProductPageLocators.AFTER_ADDING_BASKET_PRICE)
        return x_element.text





#class BasketPage(BasePage):
#    def should_be_basket_page(self):
#        self.should_be_in_basket_link()
#        self.shold_be_basket_book_name()
#        self.get_in_basket_book_name()

#    def should_be_in_basket_link(self):
#        assert self.is_element_present(*ProductBasketIn.BASKET_URL), "Wrong url - wrong page."

#    def shold_be_basket_book_name(self):
#        assert self.is_element_present(*ProductBasketIn.BASKET_BOOK_NAME), "Book name is absent."

#    def get_in_basket_book_name(self):
#        x_element = self.browser.find_element(*ProductBasketIn.BASKET_BOOK_NAME)
#        return x_element.text


