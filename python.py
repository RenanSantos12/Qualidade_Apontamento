from playwright.sync_api import sync_playwright
from time import sleep
from datetime import datetime

with sync_playwright() as playwright_:
        browser_ = playwright_.chromium.launch(headless=False)
        context_ = browser_.new_context()
        page = context_.new_page()

        dia_atual = datetime.now().day
        print(dia_atual)
        page.goto("https://forms.clickup.com/9013267565/f/8ckq33d-5753/3E2W0RUBRY1S9V29OO")
        sleep(1.5)
        page.locator("[data-test=\"form__body-item__RE\"] [data-test=\"select__dropdown__toggle\"]").click()
        sleep(1)
        page.locator("[data-test=\"select__search-field\"]").fill("Renan Santos")
        sleep(1)
        page.get_by_role("option", name="- RENAN SANTOS ARAUJO").locator("div").nth(1).click()
        sleep(1)
        page.locator(
            "[data-test=\"form__body-item__Cliente - Projeto\"] [data-test=\"select__dropdown__toggle\"]").click()
        sleep(1)
        page.locator("[data-test=\"select__search-field\"]").fill("QU")
        sleep(1)
        page.get_by_role("option", name="Paranoá|Produtos - RPA").locator("div").nth(1).click()
        sleep(1)
        page.locator("[data-test=\"form__date-picker-input-start-date\"]").click()
        sleep(1)
        page.get_by_label(str(dia_atual)).first.click()
        sleep(1)
        page.get_by_role("spinbutton", name="Hour").fill("08")
        sleep(1)
        check_manha =  '/html/body/div[1]/div[3]/span[2]'
        if not check_manha:
                page.get_by_text("PM").nth(1).click()
        sleep(1)
        page.get_by_role("button", name="Selecione a data de vencimento").click()
        sleep(0.5)
        page.get_by_label(str(dia_atual)).nth(1).click()
        if '/html/body/div[2]/div[3]/span[2]':
                page.get_by_text("AM").nth(4).click()
        sleep(1)
        page.get_by_role("spinbutton", name="Hour").fill("03")
        sleep(2)
        page.locator("[data-test=\"form__submit-btn\"]").click()
        print(3)
print('concluido')


