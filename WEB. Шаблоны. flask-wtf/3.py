from flask import Flask, render_template


app = Flask(__name__)


@app.route('/list_prof/<list>')
def list_prof(list):
    profs = [
        'Пилот',
        'Строитель',
        'Экзобиолог',
        'Врач',
        'Водитель дирижаблей',
        'Штурман',
        'Киберинженер',
        'Оператор марсохода',
        'Метеоролог',
        'Инженер по терраформированию',
        'Терроформирователь',
        'Баласт'
    ]
    params = {
        'title': 'Марсианские профессии',
        'profs': profs,
        'vid': list,
    }
    return render_template('list_prof.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')