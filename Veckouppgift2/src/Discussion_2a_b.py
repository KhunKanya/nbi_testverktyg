#Betrakta https://lejonmanen.github.io/agile-helper/ . Skriv en user story som beskriver att användaren ska kunna läsa hur man gör en "sprint retrospective".

import re
from playwright.sync_api import Page, expect
"""user story:
            [U2] som en användare, vill jag kunna läsa hur man genomför en sprint restropective, så att jag kan förstå och genomföra på rätt sätt.

            Acceptanskriterier:
            [A1] Det ska finns en knappen texten "Last"
            [A2] Användaren ska kunna klicka på knappen "Sprint Retrospective"
            [A3] När knappen klickas ska en ny vy visas information
            [A4] En rubrik med texten "Sprint retrospective" ska visa på websidan

            Scenario:
            1. Klicka på knappen "Last"
            2. Klicka på knappen ska en ny vy visas information om "Sprint Retrospective"
            3. Rubriken "Sprint Retrospective" ska vara synlig på webbsidan.
            """
# Implicit  : Kontrollerar att sidans titel innehåller orden "Agil helper"
def test_has_title(page: Page):
    page.goto("https://lejonmanen.github.io/agile-helper/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Agile helper"))

# Explicit : Testar funtionerna som kan ses på webbsidan
def test_view_sprint_restrospective(page: Page):

    page.goto("https://lejonmanen.github.io/agile-helper/")

    button_locator = page.get_by_role("button")
    last_button = button_locator.get_by_text( re.compile("Last") )
    last_button.click(timeout=100)

    sprint_retro_button = page.get_by_role("button").get_by_text( re.compile("Sprint retrospective") ) # Explicit : Testar att knapparna till 'Sprint Retrospective' visas och fungerar korrekt.
    expect(sprint_retro_button).to_have_count(1, timeout=100)  # Locator assertion
    sprint_retro_button.click()

    heading = page.get_by_role("heading").get_by_text( re.compile("Sprint retrospective") )
    expect(heading).to_be_visible(timeout=100)
