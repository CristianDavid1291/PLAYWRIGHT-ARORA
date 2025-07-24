import pytest
import allure
from pages import HomePage
from utilities import APP_LOGGER as log

class TestHomePage:

    @allure.feature("Home Page - Navigation new Cars")
    @allure.severity(allure.severity_level.MINOR)
    def test_finding_new_cars(self, browser_instance, browser_name):
        with allure.step("Executing test_finding_new_cars"):
            log.info(f"TEST: Starting test for navigating to new cars section with {browser_name}")
            home_page = HomePage(browser_instance)
            home_page.go_to_new_cars()
            log.info("TEST: Home Page - Navigation new Cars completed")


