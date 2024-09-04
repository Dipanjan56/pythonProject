from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'VeryHardToGuess'


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/')
def hello():
    if not check_login():
        return 'You NOT currently logged in'
    return 'Hello from the simple webapp.'


"""
Why not like this? 

    if session['logged_in']:
        return 'Hello from the simple webapp.'

Answer: We are not checking the session[logged_in] as False because if there is no key [which is at the start of the app run]
it will throw key error.
Sp instead we are deleting the key while logging out and checking on other method 
if the key really exists in the dictionary or  not, thus by avoiding the KeyError
"""


@app.route('/page1')
def page1():
    if not check_login():
        return 'You NOT currently logged in'
    return 'This is page 1.'


@app.route('/page2')
def page2():
    if not check_login():
        return 'You NOT currently logged in'
    return 'This is page 2.'


@app.route('/page3')
def page3():
    if not check_login():
        return 'You NOT currently logged in'
    return 'This is page 3.'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


@app.route('/status')
def _check_status() -> str:
    if not check_login():
        return 'You NOT currently logged in'
    return 'You are currently logged in'


def check_login() -> bool:
    if 'logged_in' in session:
        return True
    return False


if __name__ == '__main__':
    app.run(debug=True)
