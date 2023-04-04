import sqlite3

from flask import current_app, g


def get_db():
    if 'db' not in g:

        if current_app.config['DATABASE_NAME'] is None and current_app.config['DATABASE_URL'] is None:
            current_app.config['DATABASE_NAME'] = 'my_database.db'

        if current_app.config['DATABASE_NAME'] is not None and current_app.config['DATABASE_URL'] is not None:
            current_app.config['DATABASE_NAME'] = None

        url = None
        if current_app.config['DATABASE_NAME'] is None and current_app.config['DATABASE_URL'] is not None:
            url = current_app.config['DATABASE_URI']

        if current_app.config['DATABASE_NAME'] is not None and current_app.config['DATABASE_URL'] is None:
            url = current_app.root_path + '/' + current_app.config['DATABASE_NAME']

        g.db = sqlite3.connect(url, detect_types=sqlite3.PARSE_DECLTYPES)
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
