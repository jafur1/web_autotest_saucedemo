from dataclasses import dataclass

@dataclass
class User:
    username: str
    password: str

class Users:
    STANDARD_USER = User(
        username="standard_user",
        password="secret_sauce"
    )
    STANDARD_INCORRECT_PASSWORD_USER = User(
        username="standard_user",
        password="1234"
    )
    LOCKED_OUT_USER = User(
        username="locked_out_user",
        password="secret_sauce"
    )
    PROBLEM_USER = User(
        username="problem_user",
        password="secret_sauce"
    )
    PERFORMANCE_GLITCH_USER = User(
        username="performance_glitch_user",
        password="secret_sauce"
    )
    ERROR_USER = User(
        username="error_user",
        password="secret_sauce"
    )
    VISUAL_USER = User(
        username="visual_user",
        password="secret_sauce"
    )
