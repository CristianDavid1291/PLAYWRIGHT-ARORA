class HomePageLocators:

    __NEW_CARS_TEXT = "NEW CARS"
    __NEW_CARS_LINK_NAME = "Find New Cars"

    @staticmethod
    def get_new_cars_navigation_button(page):
        return page.get_by_text(HomePageLocators.__NEW_CARS_TEXT, exact=True)

    @staticmethod
    def get_new_cars_link(page):
        return page.get_by_role("link", name=HomePageLocators.__NEW_CARS_LINK_NAME)