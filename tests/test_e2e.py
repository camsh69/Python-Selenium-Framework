from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("getting all the card titles")
        checkOutPage = homePage.shopItems()

        cards = checkOutPage.getCardTitles()
        i = -1
        for card in cards:
            i += 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.selectCheckOutBtn().click()

        confirmPage = checkOutPage.selectCheckOutBtn2()

        log.info("Entering country name as 'ind'")
        confirmPage.selectLocationBox().send_keys("ind")

        self.verifyLinkPresence("India")

        confirmPage.selectCountryText().click()

        confirmPage.selectCheckBox().click()

        confirmPage.selectPurchaseBtn().click()

        successText = confirmPage.getSuccessText().text
        log.info(f"Text received from application is {successText}")

        assert "Success! Thank you!" in successText
