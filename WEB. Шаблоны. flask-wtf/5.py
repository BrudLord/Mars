from flask import redirect, Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username1 = StringField('id астронавта', validators=[DataRequired()])
    password1 = PasswordField('Пароль астронавта', validators=[DataRequired()])
    username2 = StringField('id капитана', validators=[DataRequired()])
    password2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    params = {
        'form': form,
        'title': 'Аварийный доступ',
    }
    return render_template('alarm_form.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')