from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from features.test_scenarios.pages.BasePage import BasePage


class LoginPage(BasePage):
    PATH = 'C:\Program Files (x86)\Chromedriver.exe'
    URL = 'https://biochempro100.pl/moje-konto/'
    # locators:
    USERNAME = 'username'  # id
    PASSWORD = 'password'  # id
    LOGIN = 'login'  # name
    ERROR = 'woocommerce-error'  # class

    def __init__(self, driver):
        super().__init__(driver)

    def open_site(self):
        driver = webdriver.Chrome(self.PATH)
        driver.get(self.URL)
        driver.maximize_window()
        driver.implicitly_wait(15)

    def visible_element_by_id(self, id_locator):
        element = self.driver.find_element(By.ID, id_locator)
        WebDriverWait(self.driver, 15).until(element.is_displayed())
        if element.is_displayed():
            print("Element found")
        else:
            print("Element not found")

    def visible_element_by_name(self, name_locator):
        element = self.driver.find_element_by_name(name_locator)
        if element.is_displayed():
            print("Element found")
        else:
            print("Element not found")

    def visible_element_by_class(self, class_locator):
        element = self.driver.find_element(By.CLASS_NAME, class_locator)
        WebDriverWait(self.driver, 15).until(element.is_displayed())
        if element.is_displayed():
            print("Element found")
        else:
            print("Element not found")

    def find_element(self, id_locator):
        element = self.driver.find_element(By.ID, id_locator)
        return element.is_displayed()

    def clear_form(self, id_locator):
        element = self.driver.find_element(By.ID, id_locator)
        element.clear()

    def input_keys(self, id_locator, keys):
        element = self.driver.find_element(By.ID, id_locator)
        element.clear()
        element.send_keys(keys)

    def wait(self, time=5):
        self.driver.implicitly_wait(time)


class Locators:
    # locators:
    username = 'username'  # id
    password = 'password'  # id
    login = 'login'  # name
    error = 'woocommerce-error'  # class
