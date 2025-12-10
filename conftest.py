import pytest
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def login_page(page):
    login_page = LoginPage(page)
    login_page.navigate("")
    return login_page