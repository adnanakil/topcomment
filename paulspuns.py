#all the imports
import os
import sqlite3
import readapi
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_bootstrap import Bootstrap

#create the app
app = Flask(__name__)
app.config.from_object(__name__)


# Load default config and override config from an env variable
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, 'paulspuns.db'),
	DEBUG=True,
	SECRET_KEY = 'development key',
	USERNAME = 'admin',
	PASSWORD = 'default'
))

app.config.from_envvar('PAULSPUNS_SETTINGS', silent=True)



def connect_db():
	"""Connects to the specific db"""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv


def get_db():
	"""Opens a new db connection if there is none yet for the current app context"""
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db




@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



@app.route('/')
def show_puns():
	zipped = readapi.story()
	db = get_db()
	cur = db.execute('select puntext from puns order by id desc')
	entries = cur.fetchall()
	return render_template('show_entries.html', entries=entries, zipped=zipped)

@app.route('/add', methods=['POST'])
def add_entry():
	# if not session.get('logged_in'):
	# 	abort(401)
	print "you made it to this page"
	print request.form['puntext']
	db = get_db()
	db.execute('insert into puns (puntext) values (?)', [request.form['puntext']])
	db.commit()
	flash('new entry was successful')
	return redirect(url_for('show_puns'))




if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	app.run()




