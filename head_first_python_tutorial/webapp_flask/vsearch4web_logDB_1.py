from flask import Flask, render_template, request, redirect, escape
from util_functions import search4letters

# Steps to configure MariaDB(mysql Database)
# 1. install mysql server -> brew install mariadb
# 2. install mysql database driver for python -> pip3 install mysql-connector-python
# 3. create webapps DB and tables ->
# 4. create code with work with oyr webappsDB and tables

# Mechanism <-> your code -> python's DB API <-> mysql-connector/driver -> mysql DB

# Create DB and tables
# 1. connect to mysql server via root user -> sudo mysql -u root
# 2. it will enter into mariaDB server -> create database vsearchlogDB
# 3. create new user to access the DB -> CREATE USER test_user@localhost IDENTIFIED BY 'Test@123';
# 4. if u want to see the user list -> SELECT user, host FROM mysql.user;
# 5. now give access of the vsearchlogDB to this user-> grant all privileges on vsearchlogDB.* to test_user@localhost identified by 'Test@123' with grant option;
# 6. now enter into the DB using this user creds -> mysql -u test_user -p vsearchlogDB [here we dont need to specify local host as system automatically add it]
# ebter with the pass word
# 7. now create table using a structure ->
# create table log (
# id int auto_increment primary key,
# ts timestamp default current_timestamp,
# phrase varchar(128) not null,
# letters varchar(32) not null,
# ip varchar(16) not null,
# browser_string varchar(256) not null,
# results varchar(64) not null);

# now if u want to check the table -> describe log

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    dbconfig = {'host': '127.0.0.1',
                'user': 'test_user',
                'password': 'Test@123',
                'database': 'vsearchlogDB', }
    import mysql.connector
    conn = mysql.connector.connect(**dbconfig)
    cursor = conn.cursor()
    _SQL = """insert into log 
    (phrase, letters, ip, browser_string, results)
     values 
     (%s, %s, %s, %s, %s)"""
    print(req.user_agent.browser)
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          'chrome',
                          res,))
    conn.commit()
    # this is very important step, as if you dont commit, then immediately you may not see the results in DB as
    # db always do catching for insert operatiom as its very expensive operation and
    # insert all the data after some time into the tables
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results, )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""
    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)

# this 'dunder name dunder main' used to make the system understand if its running locally or not
# as all the apps are hosted somewhere in the cloud
