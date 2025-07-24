import pytest


@pytest.fixture()
def browser_instance(page):
    page.goto("/")
    yield page
    page.close()
