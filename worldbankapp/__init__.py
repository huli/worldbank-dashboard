from flask import Flask

# The position of this line is important!
app = Flask(__name__)

from worldbankapp import routes

