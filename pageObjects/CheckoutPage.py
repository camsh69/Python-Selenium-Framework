from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")

    def getProducts(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getProductName(self):
        return self.find_element(*CheckOutPage.productName)
