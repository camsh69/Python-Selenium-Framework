from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestHomePAge(BaseClass):

    def test_formSubmission(self):
        homepage = HomePage(self.driver)

        homepage.selectName().send_keys("Campbell")

        homepage.selectEmail().send_keys('dummy@email.com')

        homepage.selectPassword().send_keys('Password')

        homepage.selectCheckBox().click()

        self.selectOptionByText(homepage.selectGender(), "Female")

        homepage.selectSubmit().click()

        assert "success" in homepage.selectMessage().text
