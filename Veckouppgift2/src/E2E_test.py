import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

def click_button_by_text(page: Page, button_text: str):
    button_locator = page.get_by_role("button").get_by_text(re.compile(button_text))
    expect(button_locator).to_have_count(1, timeout=100)  # Locator assertion
    button_locator.click(timeout=100)

def test_view_sprint_planning(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    click_button_by_text(page, "First")
    click_button_by_text(page, "Sprint planning")

    sp_heading = page.get_by_role("heading").get_by_text("Sprint planning")
    expect(sp_heading).to_be_visible()

def test_view_daily_standup(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    click_button_by_text(page, "Somewhere in the middle")
    click_button_by_text(page, "Daily standup")

    heading = page.get_by_role("heading").get_by_text("Daily standup")
    expect(heading).to_be_visible(timeout=100)

def test_view_sprint_retrospective(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    click_button_by_text(page, "Last")
    click_button_by_text(page, "Sprint retrospective")

    heading = page.get_by_role("heading").get_by_text("Sprint retrospective")
    expect(heading).to_be_visible(timeout=100)

def test_over_and_return_to_main_menu(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")
    click_button_by_text(page, "First")
    click_button_by_text(page, "Somewhere in the middle")
    click_button_by_text(page, "Last")

    click_button_by_text(page, "Start over")

    main_heading = page.get_by_role("heading").get_by_text(re.compile("Agile helper"))
    expect(main_heading).to_be_visible(timeout=100)

