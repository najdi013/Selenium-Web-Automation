from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

PATH = "C:\Program Files (x86)\Chromedriver.exe"

# locators:
username = "username"  # id
password = "password"  # id
login = "login"  # name
error = "woocommerce-error"  # class


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        driver = webdriver.Chrome(PATH)
        driver.maximize_window()
        driver.implicitly_wait(5)

    def open_site(self, url):
        self.driver.get(url)

    def visible_element(self, id_locator):
        element = self.driver.find_element(By.ID, id_locator)
        WebDriverWait(self.driver, 10).until(element.is_displayed)
        return element.is_displayed()

    def wait(self, time):
        self.driver.implicitly_wait(time)
