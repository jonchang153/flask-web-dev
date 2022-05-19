from flask import Flask, g, render_template, request

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
