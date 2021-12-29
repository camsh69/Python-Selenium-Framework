from selenium.webdriver.common.by import By
from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOutBtn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutBtn2 = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def selectCheckOutBtn(self):
        return self.driver.find_element(*CheckOutPage.checkOutBtn)

    def selectCheckOutBtn2(self):
        self.driver.find_element(*CheckOutPage.checkOutBtn2).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage
