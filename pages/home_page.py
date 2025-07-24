from .locators import HomePageLocators
from utilities.log_util import Logger
import allure

class HomePage:

    log = Logger.log()

    def __init__(self, page):
        self.page = page

    def go_to_new_cars(self):
        with allure.step("Hover to the New Cars section"):
            HomePageLocators.get_new_cars_navigation_button(self.page).hover()
            self.log.info(f"Hovered over the new cars navigation button")
        with allure.step("Click on the New Cars link"):    
            HomePageLocators.get_new_cars_link(self.page).click()
            self.log.info("Clicked on the new cars link.")

    def go_to_used_cars():
        pass

    def go_to_search_cars():
        pass