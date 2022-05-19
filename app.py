from flask import Flask, g, render_template, request
import sqlite3

# import sklearn as sk
# import matplotlib.pyplot as plt
# import numpy as np

# from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
# from matplotlib.figure import Figure

# import io
# import base64



app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def submit():
    return render_template('submit.html')

@app.route('/view/')
def view():
    return render_template('view.html')

def get_message_db():
    # write some helpful comments here
    try:
        return g.message_db
    except:
        g.message_db = sqlite3.connect("messages_db.sqlite")
        cmd = '' # replace this with your SQL query
        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db
