import re
import time
from email.quoprimime import body_check
from os import remove

import playwright.sync_api
from playwright.sync_api import Page, expect
from requests import delete


# ( Hela User stories, Acceptanskriterier, Testscenarier >>> README.md )

def test_add_timer_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    timer_button = page.get_by_role("button")
    add_timer_button = timer_button.get_by_text(re.compile("Add timer"))
    add_timer_button.click()

    timer_locator = page.locator(".timer")
    expect(timer_locator).to_have_count(1, timeout=100)

def test_remove_timer_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    timer_button = page.get_by_role("button")
    add_timer_button = timer_button.get_by_text(re.compile("Add timer"))
    add_timer_button.click()

    timer_locator = page.locator(".timer")
    expect(timer_locator).to_have_count(1, timeout=100)

    remove_button = page.locator(".icon.close").first
    remove_button.click()

    expect(timer_locator).to_have_count(0, timeout=100)

def test_add_note_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    add_note = page.get_by_role("button")
    add_note_button = add_note.get_by_text(re.compile("Add note"))
    add_note_button.click()

    add_note_locator = page.locator(".note")
    expect(add_note_locator).to_have_count(1, timeout=100)

def test_remove_note_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    add_note = page.get_by_role("button")
    add_note_button = add_note.get_by_text(re.compile("Add note"))
    add_note_button.click()

    add_note_locator = page.locator(".note")
    expect(add_note_locator).to_have_count(1, timeout=100)

    remove_note_button = page.locator(".icon.close").first
    remove_note_button.click()
    expect(add_note_locator).to_have_count(0, timeout=100)

def test_change_timer_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    timer_button = page.get_by_role("button")
    add_timer_button = timer_button.get_by_text(re.compile("Add timer"))
    add_timer_button.click()

    setting_button = page.locator(".icon.settings")
    setting_button.click()
    expect(setting_button).to_be_visible()


def test_start_time_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    timer_button = page.get_by_role("button")
    add_timer_button = timer_button.get_by_text(re.compile("Add timer"))
    add_timer_button.click()

    start_button = page.get_by_role("button")
    start_time_button = start_button.get_by_text("Start")
    start_time_button.click()

    timer_locator = page.locator(".row.time")
    expect(timer_locator).to_be_visible()

def test_pause_time_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    timer_button = page.get_by_role("button")
    add_timer_button = timer_button.get_by_text(re.compile("Add timer"))
    add_timer_button.click()

    start_button = page.get_by_role("button")
    start_time_button = start_button.get_by_text("Start")
    start_time_button.click()

    pause_button = page.get_by_role("button")
    pause_time_button = pause_button.get_by_text("Pause")
    pause_time_button.click()

    pause_locator = page.locator(".timer.paused")
    expect(pause_locator).to_be_visible()

def test_reset_time_button(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    timer_button = page.get_by_role("button")
    add_timer_button = timer_button.get_by_text(re.compile("Add timer"))
    add_timer_button.click()

    start_button = page.get_by_role("button")
    start_time_button = start_button.get_by_text("Start")
    start_time_button.click()

    reset_button =  page.get_by_role("button")
    reset_time_button = reset_button.get_by_text("Reset")
    reset_time_button.click()

    reset_locator = page.locator(".timer.paused")
    expect(reset_locator).to_be_visible()

def test_change_theme_color(page: Page):
    page.goto("https://lejonmanen.github.io/timer-vue/")

    theme_button = page.get_by_role("button")
    dark_theme_button = theme_button.get_by_text(re.compile("Dark"))
    dark_theme_button.click()

    body_theme = page.locator("body")
    expect(body_theme).to_have_attribute("Dark")




























































