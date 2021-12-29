from selenium.webdriver.common.by import By
from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, 'name')
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.ID, 'exampleInputPassword1')
    checkBox = (By.ID, 'exampleCheck1')
    gender = (By.ID, 'exampleFormControlSelect1')
    submit = (By.XPATH, "//input[@type='submit']")
    message = (By.CLASS_NAME, 'alert-success')

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def selectName(self):
        return self.driver.find_element(*HomePage.name)

    def selectEmail(self):
        return self.driver.find_element(*HomePage.email)

    def selectPassword(self):
        return self.driver.find_element(*HomePage.password)

    def selectCheckBox(self):
        return self.driver.find_element(*HomePage.checkBox)

    def selectSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def selectMessage(self):
        return self.driver.find_element(*HomePage.message)

    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)
