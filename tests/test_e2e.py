import pytest
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestOne(BaseClass):

    def test_e2e(self):

        self.driver.get("https://rahulshettyacademy.com/angularpractice/")
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
        products = self.driver.find_elements(
            By.XPATH, "//div[@class='card h-100']")

        # //div[@class='card h-100']/div/h4/a
        # product =//div[@class='card h-100']
        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
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
