from functools import wraps

"""when creating you own decorator always import, then use 'functools' module's 'wraps' function"""


def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function.

        # 2. Call the decorated function as required, returning its
        #    results if needed.
        return func(*args, **kwargs)

    # 3. Code to execute INSTEAD of calling the decorated function.
    return wrapper
