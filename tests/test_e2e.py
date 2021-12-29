from utilities.BaseClass import BaseClass
from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()

        checkOutPage = CheckOutPage(self.driver)
        products = checkOutPage.getProducts()

        for product in products:
            productName = product.text
            if productName == "Nonsense":
                print(productName)
                # Add item into cart
                product.find_element(By.XPATH, "div/button").click()

        self.driver.find_element(
            By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        self.driver.find_element(
            By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 7)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH,
                                 "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(
            By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText

        # self.driver.get_screenshot_as_file("screen.png")
