from behave import *
from selenium.webdriver.common.by import By
from features.test_scenarios.pages.LoginPage import LoginPage, Locators


@given('Launch browser')
def launch_browser(context):
    context.lp = LoginPage(context)
    context.loc = Locators()


@when('Open the https://biochempro100.pl/moje-konto/ website')
def open_website(context):
    context.lp.open_site()


@then('Login form is visible')
def visible_login(context):
    context.lp.visible_element_by_name(context.loc.login)


@step('Insert username "{username}" and "{password}"')
def input_user_password(context, username, password):
    context.lp.input_keys(context.loc.username, username)
    context.lp.input_keys(context.loc.password, password)


@step("Click on the login button")
def login_click(context):
    context.login_el = context.lp.visible_element_by_name(context.loc.login)
    context.login_el.click()


@then("Login failed and invalid input data error is displayed")
def failed_login(context):
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
    if context.username_el.is_displayed():
        context.driver.implicitly_wait(5)
        context.error_loc = "woocommerce-error"  # class
        context.error_el = context.driver.find_element(By.CLASS_NAME, context.error_loc)
        context.error_el.is_displayed()
        return True
