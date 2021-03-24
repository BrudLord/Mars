from flask import Flask, render_template


app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    if 'инженер' in prof or 'строитель' in prof:
        params = {
            'title': 'Training',
            'tr': 'Инженерные тренажеры',
            'im': 'it.jpg'
        }
    else:
        params = {
            'title': 'Training',
            'tr': 'Научные симуляторы',
            'im': 'ns.jpg'
        }
    return render_template('training.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')