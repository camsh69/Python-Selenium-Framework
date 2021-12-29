import pytest
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        homepage = HomePage(self.driver)

        homepage.selectName().send_keys(getData["firstname"])

        homepage.selectEmail().send_keys(getData["email"])

        homepage.selectPassword().send_keys(getData["password"])

        homepage.selectCheckBox().click()

        self.selectOptionByText(homepage.selectGender(), getData["gender"])

        homepage.selectSubmit().click()

        assert "success" in homepage.selectMessage().text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param
