from playwright.sync_api import sync_playwright
from datetime import datetime
from time import sleep
import random


class Apontamento:

    def __init__(self):
        # self.dia_atual = datetime.now().strftime('%d').lstrip('0')
        # self.dia_mes_atual = datetime.now().strftime('%m')
        # self.mes_ = datetime.today().strftime('%B')
        self.dia_atual = int(31)
        self.mes_ = 'July'
        self.trabalho = ['Fiscal faturamento', 'RPA Qualidade', 'RPA CND']
        print(self.dia_atual)
        print(self.mes_)

    def parte1(self, page):
        page.goto("https://forms.clickup.com/9013267565/f/8ckq33d-9313/K13NOYVFNI70YT4ALA")
        sleep(5)
        page.locator("[data-test=\"form__body-item__RE\"] [data-test=\"select__dropdown__toggle\"]").click()
        sleep(1)
        page.locator("[data-test=\"select__search-field\"]").fill("Renan Santos")
        sleep(1)
        page.get_by_role("option", name="- RENAN SANTOS ARAUJO").locator("div").nth(1.5).click()
        sleep(1)
        page.locator(
            "[data-test=\"form__body-item__Cliente - Projeto\"] [data-test=\"select__dropdown__toggle\"]").click()
        sleep(1)
        projeto = random.choice(self.trabalho)
        print(projeto)
        page.locator("[data-test=\"select__search-field\"]").fill(projeto)
        sleep(1)
        page.get_by_role("option", name=projeto).locator("div").nth(1.5).click()
        sleep(1)
        page.locator("[data-test=\"form__date-picker-input-start-date\"]").click()
        sleep(1)
        page.locator("[data-test=\"form__body-item__Start date\"]").get_by_label(
            f"{self.mes_} {self.dia_atual},").click()
        sleep(1)
        page.get_by_role("spinbutton", name="Hour").fill("08")
        sleep(1)
        print(1)
        check_manha = '/html/body/div[1]/div[3]/span[2]'
        if not check_manha:
            print(2)
            page.get_by_text("PM").nth(1).click()
        sleep(1)
        print(3)
        page.get_by_role("button", name="Select Due Date").click()
        sleep(1)
        page.get_by_label(f"{self.mes_} {self.dia_atual},").nth(1).click()
        if '/html/body/div[2]/div[3]/span[2]':
            page.get_by_text("AM").nth(4).click()
        sleep(1)
        page.get_by_role("spinbutton", name="Hour").fill("12")
        sleep(2)
        page.get_by_role("textbox", name="Unidade de Produção").click()
        sleep(1)
        page.locator("[data-test=\"form__submit-btn\"]").click()
        sleep(5)
        print('concluido')
    def parte2(self, page):
        page.goto("https://forms.clickup.com/9013267565/f/8ckq33d-9313/K13NOYVFNI70YT4ALA")
        sleep(5)
        page.locator("[data-test=\"form__body-item__RE\"] [data-test=\"select__dropdown__toggle\"]").click()
        sleep(1)
        page.locator("[data-test=\"select__search-field\"]").fill("Renan Santos")
        sleep(1)
        page.get_by_role("option", name="- RENAN SANTOS ARAUJO").locator("div").nth(1.5).click()
        sleep(1)
        page.locator(
            "[data-test=\"form__body-item__Cliente - Projeto\"] [data-test=\"select__dropdown__toggle\"]").click()
        sleep(1)
        projeto = random.choice(self.trabalho)
        print(projeto)
        page.locator("[data-test=\"select__search-field\"]").fill(projeto)
        sleep(1)
        page.get_by_role("option", name=projeto).locator("div").nth(1.5).click()
        sleep(1)
        page.locator("[data-test=\"form__date-picker-input-start-date\"]").click(force=True)
        sleep(1)
        page.locator("[data-test=\"form__body-item__Start date\"]").get_by_label(
            f"{self.mes_} {self.dia_atual},").click()
        sleep(1)
        page.locator("[data-test=\"form__body-item__Start date\"]").get_by_text("AM").nth(1).click()
        sleep(1)
        page.get_by_role("spinbutton", name="Hour").fill("01")
        sleep(1)
        page.get_by_role("button", name="Select Due Date").click()
        sleep(1)
        page.get_by_label(f"{self.mes_} {self.dia_atual},").nth(1).click()
        sleep(0.5)
        page.get_by_role("spinbutton", name="Hour").fill("03")
        sleep(2)
        page.get_by_role("textbox", name="Unidade de Produção").click()
        sleep(1)
        page.locator("[data-test=\"form__submit-btn\"]").click()
        sleep(3)
        print('concluido')

if __name__ == "__main__":
    with sync_playwright() as playwright_:
        browser_ = playwright_.chromium.launch(headless=False)
        context_ = browser_.new_context()
        page_ = context_.new_page()

        execute = Apontamento()
        execute.parte1(page_)
        execute.parte2(page_)



