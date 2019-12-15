import math

from selenium.common.exceptions import NoAlertPresentException

from .base_page import BasePage#, solve_quiz_and_get_code
from .locators import ProductPageLocators, BasePageLocators



class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button_add_to_basket()
        self.should_be_book_name()
        self.should_be_book_price()
        self.should_be_basket_price()
        self.should_be_to_basket_link()
        self.should_be_present_search_button()
        self.should_be_lang_select_button()
        self.should_be_lang_select_button()


    def should_be_button_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.TO_BASKET_BTN), "To basket button is absent."

#    def should_be_product_link_xmass(self,link_postfix):
        #assert self.is_element_present(*ProductPageLocators.MARY_LINK), "Wrong url - wrong page."
        #"+(str(self.browser.current_url.find(u"promo=newYear")))+"
#        assert link_postfix in str(self.browser.current_url), "Login link is not found 'login' : "+str(self.browser.current_url)
        #assert self.is_element_present(*ProductPageLocators.MARY_LINK), "Wrong url - wrong page : "+self.is_element_present(*ProductPageLocators.MARY_LINK)

    def should_be_book_name(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_NAME), "Book name is absent."

    def should_be_book_price(self):
        assert self.is_element_present(*ProductPageLocators.BOOK_PRICE), "Book price is absent."

    def should_be_basket_price(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), "Book price is absent."

    def should_be_to_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.GO_TO_BASKET), "Link into basket is absent."

    def should_be_language_preseted(self):
        assert self.is_element_present(*ProductPageLocators.PRESETED_LANG), "Preseted lang not ru."

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


    def get_adding_result_book_name(self):
        x_element = self.browser.find_element(*ProductPageLocators.AFTER_ADDING_BOOK_NAME)
        return x_element.text


    def get_adding_result_basket_price(self):
        x_element = self.browser.find_element(*ProductPageLocators.AFTER_ADDING_BASKET_PRICE)
        return x_element.text

    def compare_book_price_with_top_basket_price(self,first_price):
        #first_price = 0
        x_element = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        assert first_price != str(x_element.text), "Book price on page : " + first_price + " not correspond basket price : " + str(x_element.text)



    def find_ordered_book_price_in_after_click_changes(self,price):
        #price = ""
        x_element = self.browser.find_element(*ProductPageLocators.AFTER_ADDING_BASKET_PRICE)
        assert price == str(x_element.text), "Book price on page : " + price + " not correspond basket price : " + str(x_element.text)

    def find_ordered_book_name_in_after_click_changes(self,book_name):
        #book_name = ""
        x_element = self.browser.find_element(*ProductPageLocators.AFTER_ADDING_BOOK_NAME)
        assert book_name == str(x_element.text), "Book name on page : " + book_name + " not correspond basket name : " + str(x_element.text)

    def should_be_present_search_button(self):
        assert self.is_element_present(*ProductPageLocators.SEARCH_BUTTON), "search button is absent."


    def should_be_lang_select_button(self):
       assert self.is_element_present(*ProductPageLocators.SEARCH_BUTTON), "search button is absent."


    #example should_not_be
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


    #example should_not_be after several seconds
    def should_not_be_after_waited_time_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


#    def click_by_login_button(self):
#        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
#        link.click()