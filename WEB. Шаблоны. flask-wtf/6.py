from flask import Flask, render_template

app = Flask(__name__)


@app.route('/distribution')
def distribution():
    ek = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    params = {
        'title': 'Mars',
        'ek': ek,
    }
    return render_template('dist.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
