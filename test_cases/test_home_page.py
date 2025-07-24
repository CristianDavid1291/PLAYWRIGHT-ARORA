import pytest
import allure
from pages.home_page import HomePage

class TestHomePage:

    @allure.feature("Home Page - Navitation new Cars")
    @allure.severity(allure.severity_level.MINOR)
    def test_finding_new_cars(self, browser_instance):
        with allure.step("Executing test_finding_new_cars"):
            home_page = HomePage(browser_instance)
            home_page.go_to_new_cars()


