from time import sleep

from flask import Flask, render_template, request, session
from util_functions import search4letters
from head_first_python_tutorial.Context_Manager.DBcm import UseDatabase, ConnectionError, CredentialsError, SQLError
from checker import check_logged_in

# Steps to configure MariaDB(mysql Database)
# see verach4web_logDB_1.py module

app = Flask(__name__)

app.secret_key = 'VeryHardToGuess'

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'test_user',
                          'password': 'Test@123',
                          'database': 'vsearchlogDB', }


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in'


@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""

    # raise Exception("Something awful just happened.")
    sleep(15)
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              'chrome',
                              res,))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    """This will catch the error silently as if any DB connection error occurs it will only print the error on condole,
         not on the webpage
         """
    try:
        log_request(request, results)
    except Exception as err:
        print('***** Logging failed with this error:', str(err))
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
@check_logged_in
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            _SQL = """select phrase, letters, ip, browser_string, results
            from log"""
            cursor.execute(_SQL)
            contents = cursor.fetchall()
        titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
        return render_template('viewlog.html',
                               the_title='View Log',
                               the_row_titles=titles,
                               the_data=contents, )
    except ConnectionError as err:
        print('Is your DB switched on? Error: ', str(err))
    except CredentialsError as err:
        print('User-id/Password issues. Error: ', str(err))
    except SQLError as err:
        print('Is your query correct: ', str(err))
    except Exception as err:
        print('Something went wrong: ', str(err))
    return 'ERROR!'


"""here we are using ConnectionError custom exception class to make our webapp loosely coupled to mysql DB,
so that we can connect any DN we like

If we dont use ConnectorError class, then we have to import mql and instead of ConnectionError, we had to use
except mysql.connector.errors.InterfaceError as err:, which makes this webapp tightly coupled to mysql only
"""

if __name__ == '__main__':
    app.run(debug=True)

# this 'dunder name dunder main' used to make the system understand if its running locally or not
# as all the apps are hosted somewhere in the cloud
