from playwright.sync_api import sync_playwright
from datetime import datetime
from time import sleep
import random

class Apontamento:
    def __init__(self):
        self.dia_atual = datetime.now().strftime('%d').lstrip('0')
        self.dia_mes_atual = datetime.now().strftime('%m')
        self.mes_ = datetime.today().strftime('%B')
        self.trabalho = ['Fiscal faturamento', 'RPA Qualidade', 'RPA CND']
        print(self.dia_atual)
        print(self.mes_)

    def parte1(self, page):
        page.goto("https://forms.clickup.com/9013267565/f/8ckq33d-11993/5GCZKRV3FZPKLCXY1Q")
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
        page.get_by_role("spinbutton", name="Hour").fill("07")
        sleep(0.5)
        page.get_by_role("spinbutton", name="Minute").click()
        sleep(0.5)
        page.get_by_role("spinbutton", name="Minute").fill("30")
        sleep(0.5)
        page.get_by_role("spinbutton", name="Minute").press("Enter")
        sleep(1)
        #page.get_by_role("button", name="Select Due Date").click()
        #sleep(0.5)
        #page.locator("[data-test=\"form__body-item__Due date\"]").get_by_text("AM").click()
        #check_manha = '/html/body/div[1]/div[3]/span[2]'
        #if not check_manha:
        #    print(2)
        #    page.get_by_text("PM").nth(1).click()
        sleep(1)
        print(3)
        page.get_by_role("button", name="Select Due Date").click()
        sleep(0.5)
        page.locator("[data-test=\"form__body-item__Due date\"]").get_by_text("AM").click()
        sleep(0.5)
        #page.locator("[data-test=\"form__body-item__Due date\"]").get_by_label(f"{self.mes_} {self.dia_atual},").click()
        page.get_by_label(f"{self.mes_} {self.dia_atual},").nth(1).click()
        sleep(0.5)
        page.get_by_role("spinbutton", name="Hour").click()
        page.get_by_role("spinbutton", name="Hour").press("ArrowRight")
        sleep(0.5)
        page.get_by_role("spinbutton", name="Hour").fill("16")
        page.get_by_role("spinbutton", name="Minute").fill("00")
        sleep(0.5)
        page.get_by_role("spinbutton", name="Hour").press("Enter")
        page.get_by_role("textbox", name="Unidade de Produção").click()
        sleep(1)
        page.locator("[data-test=\"form__submit-btn\"]").click()
        sleep(3)


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