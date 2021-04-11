from flask import Flask, render_template
from random import choice

app = Flask(__name__)


@app.route('/member')
def training():
    f = choice(eval(open('templates/eqip.json', 'r', encoding='UTF-8').read()))
    print(f['im'])
    params = {
        'title': 'Member',
        'name': f['name'],
        'surname': f['surname'],
        'image': f['im'],
        'jobs': ', '.join(sorted(f['jobs']))
    }
    return render_template('eqip.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
