from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello World From Flask!'


app.run()

# __name__ means the current active module we are working on, so here Flask(__name__) means the flask object of the
# current active module i.e. hello_flask.py

# here @ is the function decorator.
# Function Decorator: It adjusts the behavior of an existing function without changing the function's original code
# It means, decorator allows you to take some existing code and augment it with additional behavior if needed
# decorator can be applied to classes an functions, although they are mainly applied to functions and primarily called
# as 'function decorators'

#
