from flask import Flask, g, render_template, request
import sqlite3


app = Flask(__name__)


def get_message_db():
    # write some helpful comments here
    try:
        return g.message_db
    except:
        g.message_db = sqlite3.connect("messages_db.sqlite")
        cmd = \
        """
        CREATE TABLE IF NOT EXISTS messages(
            id integer
            handle text
            message text)
        """
        cursor = g.message_db.cursor()
        cursor.execute(cmd)
        return g.message_db


def insert_message(request):
    message = request.form['message']
    handle = request.form['handle']

    db = get_message_db()

    cmd = \
    """
    SELECT COUNT(*) as id
    INSERT INTO messages VALUES (id+1, handle, message) 
    """

    cursor = db.cursor()
    cursor.execute(cmd)

    db.commit()
    db.close()

    return message, handle


@app.route('/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        insert_message(request)
        return render_template('submit.html', submitted=True)


@app.route('/view/')
def view():
    return render_template('view.html')