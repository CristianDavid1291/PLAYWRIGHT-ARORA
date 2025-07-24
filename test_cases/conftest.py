import pytest
import allure
import os
from datetime import datetime


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context to block notifications and other permissions"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080}
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    """Configure browser launch arguments for different browsers"""
    return {
        **browser_type_launch_args,
        "firefox_user_prefs": {
       #     "dom.webnotifications.enabled": False, 
        }
    }


@pytest.fixture()
def browser_instance(page):
    """Initialize browser instance and navigate to base URL"""
    page.goto("/")
    yield page


@pytest.fixture(autouse=True)
def log_on_failure(request, page):
    """Capture screenshot and logs on test failure"""
    yield
    item = request.node
    if item.rep_call.failed:
        try:
            # Crear directorios si no existen
            screenshot_dir = "screenshots"
            if not os.path.exists(screenshot_dir):
                os.makedirs(screenshot_dir)

            # Nombre único por test con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = request.node.name.replace("[", "_").replace("]", "")
            screenshot_path = f"{screenshot_dir}/failure_{test_name}_{timestamp}.png"

            # Capturar screenshot si la página está disponible
            if not page.is_closed():
                page.screenshot(path=screenshot_path, full_page=True)

                # Adjuntar a Allure con mejor metadata
                allure.attach.file(
                    screenshot_path,
                    name=f"Screenshot - {test_name}",
                    attachment_type=allure.attachment_type.PNG
                )

        except Exception as e:
            print(f"Error capturing failure artifacts: {e}")
