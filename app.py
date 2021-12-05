from flask import Flask, redirect, abort, render_template, request
import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<shortcode>')
def get(shortcode):
    link = db.read(shortcode)
    if link is None:
        abort(404)
    else:
        db.update(shortcode, 'register_click')
        return redirect(link)


@app.route('/create', methods=['POST'])
def new():
    if request.method == 'POST':
        link = request.form['link']
        shortcode = db.create(link)
        return render_template('link-created.html', link=link, shortcode=shortcode)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    db.init_db()
    app.run()
