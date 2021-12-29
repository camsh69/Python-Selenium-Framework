from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


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

        self.verifyLinkPresence("India")

        confirmPage.selectCountryText().click()

        confirmPage.selectCheckBox().click()

        confirmPage.selectPurchaseBtn().click()

        successText = confirmPage.getSuccessText().text

        assert "Success! Thank you!" in successText

        # self.driver.get_screenshot_as_file("screen.png")
