from behave import *
from features.pages.LoginPage import LoginPage, Locators


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
    context.lp.click_element_by_name(context.loc.login)


@then("Login failed and invalid input data error is displayed")
def failed_login(context):
    context.lp.visible_element_by_class(context.loc.error)


@then("Close the browser")
def browser_close(context):
    context.lp.quit()


@step('Input password "admin123"')
def input_password(context):
    context.lp.input_keys(context.loc.password, context.loc.password_in)


@then("Login failed and empty username error is displayed")
def empty_username(context):
    context.lp.visible_element_by_class(context.loc.error)


@step('Input username "admin"')
def input_username(context):
    context.lp.input_keys(context.loc.username, context.loc.username_in)


@then("Login failed and empty password error is displayed")
def empty_password(context):
    context.lp.visible_element_by_class(context.loc.error)


@step("Check if username is empty")
def empty_username(context):
    context.lp.clear_form(context.loc.username)


@step("Check if password is empty")
def empty_password(context):
    context.lp.clear_form(context.loc.password)
