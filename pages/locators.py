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
    BOOK_NAME = (By.CSS_SELECTOR, "div.row>div.col-sm-6.product_main>h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p.price_color")
    BASKET_PRICE = (By.TAG_NAME, "div strong")
    GO_TO_BASKET = (By.LINK_TEXT, "Посмотреть корзину")

    AFTER_ADDING_BASKET_PRICE = (By.CSS_SELECTOR, '#messages>div.alert.alert-safe.alert-noicon.alert-info.fade.in>div>p:nth-child(1)>strong')
    AFTER_ADDING_BOOK_NAME = (By.CSS_SELECTOR, '#messages>div:nth-child(1)>div>strong')

    SEARCH_BUTTON = (By.CSS_SELECTOR,'[value = "Найти"]')
    PRESETED_LANG = (By.CSS_SELECTOR, '.form-group .form-control [value="ru"][selected="selected"]')


    SUCCESS_MESSAGE = (By.CSS_SELECTOR,'#messages .alert-info')



