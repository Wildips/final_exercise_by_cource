from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, ".login_form")
    REGISTER_FORM = (By.CLASS_NAME, ".register_form")
    LOGIN_URL = (By.PARTIAL_LINK_TEXT, "/login/")


class ProductPageLocators():
    TO_BASKET_BTN = (By.CLASS_NAME,"btn-add-to-basket")
    MARY_LINK = (By.PARTIAL_LINK_TEXT, "/?promo=newYear")
    BOOK_NAME = (By.TAG_NAME, "div h1")
    BOOK_PRICE = (By.TAG_NAME, "p[class=price_color]")
    BASKET_PRICE = (By.TAG_NAME, "div strong")
    GO_TO_BASKET = (By.LINK_TEXT, "Посмотреть корзину")
    AFTER_ADDING_BASKET_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    AFTER_ADDING_BOOK_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')


#class ProductBasketIn():
#    BASKET_URL = (By.PARTIAL_LINK_TEXT, "/?promo=newYear")
#    BASKET_BOOK_NAME = (By.TAG_NAME, "div h1")

