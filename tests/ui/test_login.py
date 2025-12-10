from data.users import *
from data.error_messag import *
import pytest

class TestLogin:
    @pytest.mark.positive
    def test_valid_user_login(self, login_page):
        login_page.login(
            Users.STANDARD_USER.username,
            Users.STANDARD_USER.password,
        )
        assert login_page.is_logged_in()

    @pytest.mark.negative
    def test_invalid_login(self, login_page):
        login_page.login(
            Users.STANDARD_INCORRECT_PASSWORD_USER.username,
            Users.STANDARD_INCORRECT_PASSWORD_USER.password,
        )
        assert login_page.error_text() == LoginErrorMessage.STANDARD_INVALID_MESSAGE

    @pytest.mark.positive
    def test_blocked_user_login(self, login_page):
        login_page.login(
            Users.LOCKED_OUT_USER.username,
            Users.LOCKED_OUT_USER.password,
        )
        assert login_page.error_text() == LoginErrorMessage.LOCKED_OUT_USER

    @pytest.mark.positive
    def test_problem_user_login(self, login_page):
        login_page.login(
            Users.PROBLEM_USER.username,
            Users.PROBLEM_USER.password,
        )
        assert login_page.is_logged_in()


