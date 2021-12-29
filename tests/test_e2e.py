from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)

        checkOutPage = homePage.shopItems()

        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.selectCheckOutBtn().click()

        confirmPage = checkOutPage.selectCheckOutBtn2()

        confirmPage.selectLocationBox().send_keys("ind")

        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located(confirmPage.countryText))
        confirmPage.selectCountryText().click()

        confirmPage.selectCheckBox().click()

        confirmPage.selectPurchaseBtn().click()

        successText = confirmPage.getSuccessText().text

        assert "Success! Thank you!" in successText

        # self.driver.get_screenshot_as_file("screen.png")
