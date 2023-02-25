"""
# start the server -> mysql.server start
# Create DB and tables
# 1. connect to mysql server via root user -> sudo mysql -u root
# 2. it will enter into mariaDB server -> create database vsearchlogDB
# 3. create new user to access the DB -> CREATE USER test_user@localhost IDENTIFIED BY 'Test@123';
# 4. if u want to see the user list -> SELECT user, host FROM mysql.user;
# 5. now give access of the vsearchlogDB to this user-> grant all privileges on vsearchlogDB.* to test_user@localhost identified by 'Test@123' with grant option;
# 6. now enter into the DB using this user creds -> mysql -u test_user -p vsearchlogDB [here we dont need to specify local host as system automatically add it]
# enter with the pass word: Test@123
# 7. now create table using a structure ->
create table log (
id int auto_increment primary key,
ts timestamp default current_timestamp,
phrase varchar(128) not null,
letters varchar(32) not null,
ip varchar(16) not null,
browser_string varchar(256) not null,
results varchar(64) not null);

# now if u want to check the table -> describe log
"""
"""
Context management protocol =>
        It dictates any class you create must define at least two magic method: __enter__ and __exit__
        when you adhere to this protocol, your class can hook into with statement. This class is called as 'Context Manager'

        1. dunder enter [__enter__] performs setup -> when an object is used with a 'with statement', the interpreter invokes
        the objects __enter__ method before the with statement's suite start.
        this protocol further states that __enter__ return a value to the 'with' statement

        2. __init__ runs before __enter_ i.e. before your context manager's set up code


        3. dunder exit [__exit__] performs teardown -> as soon as the 'with' statement ends, interpreter invokes the __exit__
        method, which occurs after the with's suite terminates.
        as the cod ein with statement fails, __exit__ has to be ready to handle this if it happens.
"""

"""
The UseDatabase context manager for working with MySQL/MariaDB.

For more information, see Chapters 7, 8, 9, and 11 of the 2nd edition of
Head First Python.

Simple example usage:

    from DBcm import UseDatabase, SQLError

    config = { 'host': '127.0.0.1',
               'user': 'myUserid',
               'password': 'myPassword',
               'database': 'myDB' }

    with UseDatabase(config) as cursor:
        _SQL = "select * from log"
        cursor.execute(_SQL)
        data = cursor.fetchall()

Enjoy, and have fun.  (Sorry: Python 3 only, due to type hints and new syntax).

To start the mysql server locally: mysql.server start
"""

##############################################################################
# Context manager for connecting/disconnecting to a database.
##############################################################################

import mysql.connector

"""creating custom exception class to handle the database connectivity error as a generalised one"""
"""Also for Creds error and sql query error, sql throws same error -> Programming error, although the meaning of two
errors are different

Fo creds error we occurs before with statement in webapp code, so handling it __enter__ method is the right way

But for sql error, it occurs within the with statement in webapp code and then it send the exception to __exit method
do we have to handle it in __exit code with the type of error and also after the three lines -> 
cursor.commit, cursor.close, conn.close
so that it will close the connection first then will raise the Programming error
"""


class ConnectionError(Exception):
    """Raised if the backend-database cannot be connected to."""
    pass


class CredentialsError(Exception):
    """Raised if the database is up, but there's a login issue."""
    pass


class SQLError(Exception):
    """Raised if the query caused problems."""
    pass


class UseDatabase:
    def __init__(self, config: dict):
        """Add the database configuration parameters to the object.

        This class expects a single dictionary argument which needs to assign
        the appropriate values to (at least) the following keys:

            host - the IP address of the host running MySQL/MariaDB.
            user - the MySQL/MariaDB username to use.
            password - the user's password.
            database - the name of the database to use.

        For more options, refer to the mysql-connector-python documentation.
        """
        self.configuration = config

    def __enter__(self) -> 'cursor':
        """Connect to database and create a DB cursor.

        Return the database cursor to the context manager.
        Raise ConnnectionError if the database can't be found.
        Raise CredentialsError if the wrong username/password used.
        """
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err) from err
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err) from err

    def __exit__(self, exc_type, exc_value, exc_traceback):
        """Destroy the cursor as well as the connection (after committing).

        Raise ProgrammingError as an SQLError, and re-raise anything else.
        """
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
        if exc_type is mysql.connector.errors.ProgrammingError:
            raise SQLError(exc_value)
        # elif exc_type:
        #     raise exc_type(exc_value)
