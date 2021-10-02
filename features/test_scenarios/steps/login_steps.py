from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch browser')
def launch_browser(context):
    path = "C:\Program Files (x86)\Chromedriver.exe"
    context.driver = webdriver.Chrome(path)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)


@when('Open the https://biochempro100.pl/moje-konto/ website')
def open_website(context):
    website = "https://biochempro100.pl/moje-konto/"
    context.driver.get(website)


@then('Login form is visible')
def visible_login(context):
    context.username_loc = "username"  # ID
    context.password_loc = "password"  # ID
    context.username_el = context.driver.find_element(By.ID, context.username_loc)
    context.driver.implicitly_wait(5)
    return context.username_el.is_displayed()


@step('Insert username "{username}" and "{password}"')
def input_user_password(context, username, password):
    context.password_el = context.driver.find_element(By.ID, context.password_loc)
    context.username_el.clear()
    context.password_el.clear()
    context.username_el.send_keys(username)
    context.password_el.send_keys(password)


@step("Click on the login button")
def login_click(context):
    context.login_loc = "login"  # name
    context.login_el = context.driver.find_element(By.NAME, context.login_loc)
    context.login_el.click()
    context.driver.implicitly_wait(50)


@then("Login failed and invalid input data error is displayed")
def failed_login(context):
    context.driver.implicitly_wait(5)
    if context.username_el.is_displayed():
        context.driver.implicitly_wait(5)
        context.error_loc = "woocommerce-error"  # class
        context.error_el = context.driver.find_element(By.CLASS_NAME, context.error_loc)
        context.error_el.is_displayed()
        return True


@then("Close the browser")
def browser_close(context):
    context.driver.quit()


@step('Input password "admin123"')
def input_password(context):
    context.password_el.clear()
    password = 'admin123'
    context.password_el.send_keys(password)


@then("Login failed and empty username error is displayed")
def empty_username(context):
    context.driver.implicitly_wait(5)
    if context.username_el.is_displayed():
        context.driver.implicitly_wait(5)
        context.error_loc = "woocommerce-error"  # class
        context.error_el = context.driver.find_element(By.CLASS_NAME, context.error_loc)
        context.error_el.is_displayed()
        return True


@step('Input username "admin"')
def input_username(context):
    context.username_el.clear()
    username = 'admin'
    context.username_el.send_keys(username)


@then("Login failed and empty password error is displayed")
def empty_password(context):
    context.driver.implicitly_wait(5)
    if context.username_el.is_displayed():
        context.driver.implicitly_wait(5)
        context.error_loc = "woocommerce-error"  # class
        context.error_el = context.driver.find_element(By.CLASS_NAME, context.error_loc)
        context.error_el.is_displayed()
        return True
