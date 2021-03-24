from flask import Flask, render_template


app = Flask(__name__)


@app.route('/table/<a>/<b>')
def table(a, b):
    if a in ['male', 'female'] and b.isdigit():
        params = {
            'title': 'Super design',
            'a': a,
            'b': int(b)
        }
        return render_template('design.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')