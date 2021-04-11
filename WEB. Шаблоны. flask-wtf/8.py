from flask import Flask, render_template, request
from io import BytesIO
from PIL import Image
import os


app = Flask(__name__)


@app.route('/galery', methods=['POST', 'GET'])
def gal():
    if request.method == 'GET':
        print(list(os.listdir('static/img/')))
        params = {
            'title': 'Super design',
            'images': list(os.listdir('static/img2/'))
        }
        return render_template('New_car.html', **params)
    elif request.method == 'POST':
        f = request.files['file']
        im = Image.open(BytesIO(f.read())).convert('RGB')
        s = str(len(list(os.listdir('static/img2/'))) + 1)
        im.save('static/img2/' + s + '.png')
        params = {
            'title': 'Super design',
            'images': list(os.listdir('static/img2/'))
        }
        return render_template('New_car.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
