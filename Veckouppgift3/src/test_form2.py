import re
from calendar import error
from tokenize import maybe

import playwright.sync_api
from playwright.sync_api import Page, expect


def test_name_field(page: Page):
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")

    name_field = page.get_by_role("textbox").first
    expect(name_field).to_have_value(re.compile(".+"))

    error_message = "Skriv in ditt namn."
    maybe_error = page.get_by_text(error_message)
    expect(maybe_error).to_be_hidden()

    name_field.fill("")

    expect(maybe_error).to_be_visible()

def test_year_of_birth_field(page: Page):
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")

    year_field = page.get_by_role("textbox").nth(1)
    expect(year_field).to_have_value(re.compile(r"^\d{4}$"))

    error_message = "Skriv årtal med fyra siffror."
    maybe_error = page.get_by_text(error_message)
    expect(maybe_error).to_be_hidden()

    year_field.fill("")

    expect(maybe_error).to_be_visible()

def test_email_field(page: Page):
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")

    email_field = page.get_by_role("textbox").nth(2)
    expect(email_field).to_have_value(re.compile(r"(\w|[\.\-])+@\w+\.\w+"))

    error_message = "Använd formatet: email@domän.com"
    maybe_error = page.get_by_text(error_message)
    expect(maybe_error).to_be_hidden()

    email_field.fill("")

    expect(maybe_error).to_be_visible()

def test_password_field(page: Page):
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")

    password_field = page.get_by_role("textbox").nth(3)
    expect(password_field).to_have_value(re.compile(r"^.{4,}$"))

    error_massage = "Lösenordet ska vara minst 4 tecken."
    maybe_error = page.get_by_text(error_massage)
    expect(maybe_error).to_be_hidden()

    password_field.fill("")

    expect(maybe_error).to_be_visible()

def test_submit_button(page: Page):
    page.goto("https://tap-ht24-testverktyg.github.io/form-demo/")

    button = page.get_by_role("button").last
    expect(button).to_be_disabled(timeout=100)

    password_field = page.get_by_role("textbox").nth(4)
    password_field.fill("p4ssw0rd")

    expect(button).to_be_enabled(timeout=100)








