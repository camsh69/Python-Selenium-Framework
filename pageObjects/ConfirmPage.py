from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    locationBox = (By.ID, "country")
    countryText = (By.LINK_TEXT, "India")
    checkBox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseBtn = (By.CSS_SELECTOR, "[type='submit']")
    successText = (By.CLASS_NAME, "alert-success")

    def selectLocationBox(self):
        return self.driver.find_element(*ConfirmPage.locationBox)

    def selectCountryText(self):
        return self.driver.find_element(*ConfirmPage.countryText)

    def selectCheckBox(self):
        return self.driver.find_element(*ConfirmPage.checkBox)

    def selectPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchaseBtn)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)