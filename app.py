from flask import Flask, g, render_template, request
import sqlite3


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('main.html')


def get_message_db():
    try:
        return g.message_db

    except:
        g.message_db = sqlite3.connect("messages_db.sqlite")

        cmd = \
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            handle TEXT NOT NULL)
        """

        cursor = g.message_db.cursor()
        cursor.execute(cmd)

        return g.message_db


def insert_message(request):
    message = request.form['message']
    handle = request.form['handle']


    conn = get_message_db()

    cmd = \
    f"""
    INSERT INTO messages (message, handle) 
    VALUES ('{message}', '{handle}')
    """

    cursor = conn.cursor()
    cursor.execute(cmd)

    conn.commit()
    conn.close()

    return message, handle


@app.route('/submit/', methods=['POST', 'GET'])
def submit():
    if request.method == 'GET':
        return render_template('submit.html')
    else:
        try:
            message, handle = insert_message(request)
            return render_template('submit.html', submitted=True, message=message, handle=handle)
        except:
            return render_template('submit.html', error=True)



def random_messages(n):
    # https://stackoverflow.com/questions/2279706/select-random-row-from-a-sqlite-table
    conn = get_message_db()

    cmd = \
    f"""
    SELECT * FROM messages ORDER BY RANDOM() LIMIT {n}
    """

    cursor = conn.cursor()
    cursor.execute(cmd)
    result = cursor.fetchall()
    conn.close()

    return result


@app.route('/view/')
def view():
    return render_template('view.html', messages=random_messages(5))