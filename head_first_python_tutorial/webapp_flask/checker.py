from flask import session
from functools import wraps

"""when creating you own decorator always import, then use 'functools' module's 'wraps' function"""


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return 'You are NOT logged in'

    return wrapper
