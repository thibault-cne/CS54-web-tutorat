"""
    Author : Thibault Cheneviere
    Email : thibault.cheneviere@telecomnancy.eu
    Date : 13/12/2021
"""

# import needed modules
from flask import Flask, flash, redirect


app = Flask(__name__)

app.config['SECRET_KEY'] = '1sZn3QAl35qIYaoqjLbB9JxuYxqOyVN3'

# Import blueprints
## Import main blueprint
from py.blueprints.mainBP import mainBP
app.register_blueprint(mainBP)

## Import display blueprint
from py.blueprints.displayBP import displayBP
app.register_blueprint(displayBP)

## Import addCode blueprint
from py.blueprints.addCodeBP import addCodeBP
app.register_blueprint(addCodeBP)

## Import redirect blueprint
from py.blueprints.redirectBP import redirectBP
app.register_blueprint(redirectBP)


# Error 404 handler
@app.errorhandler(404)
def pageNotFound(error):
    flash("HTTP 404 Not Found", "Red_flash")
    return redirect('/display')