import sqlite3
import random
import string


DATABASE = 'db.sqlite'


def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS links (
                code TEXT PRIMARY KEY,
                link TEXT,
                clicks INTEGER
            );
        ''')


def create(link):
    with sqlite3.connect(DATABASE) as conn:
        result = conn.execute('''SELECT code FROM links WHERE link=? LIMIT 1''', (link,)).fetchone()

        if result is not None:
            return result[0]
        else:
            existing = [result[0] for result in conn.execute('''SELECT code FROM links''').fetchall()]
            while True:
                shortcode = ''.join([random.choice(string.ascii_lowercase) for _ in range(4)])
                if shortcode not in existing:
                    break

        conn.execute('''INSERT INTO links (code, link, clicks) VALUES (?,?,0)''', (shortcode, link))

    return shortcode


def read(shortcode):
    shortcode = shortcode.lower()

    with sqlite3.connect(DATABASE) as conn:
        result = conn.execute('''SELECT link FROM links WHERE code=? LIMIT 1''', (shortcode,)).fetchone()

    return result[0] if result is not None else result


def update(shortcode, method, data=None):
    shortcode = shortcode.lower()

    if method == 'register_click':
        with sqlite3.connect(DATABASE) as conn:
            conn.execute('''UPDATE links SET clicks = clicks + 1 WHERE code=?''', (shortcode,))


def delete():
    raise NotImplementedError
