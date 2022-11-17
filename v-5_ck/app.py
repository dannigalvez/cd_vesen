from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "gaman"

class MyForm(FlaskForm):
    f = StringField('Fyrirsögn', validators=[DataRequired()])
    m = TextAreaField('Meginmál', validators=[DataRequired()])
    h = StringField('Höfundur', validators=[DataRequired()])
    b = SubmitField("Skrá")

gogn = {}

@app.route('/', methods=["POST", "GET"])
def index():
    form = MyForm()
    global gogn # verðum að hafa þetta inni til að hægt sé að vísa í breytuna og uppfæra í fallinu

    if request.form and form.validate_on_submit(): # erum að koma úr forminu með gögn 
        print(form.data)
        gogn = {"f":form.f.data,"m":form.m.data,"h":form.h.data}
        flash("Jíbbí jajei mófóerinn...")
        return render_template('index.html', g=gogn, lengd=len(gogn))
    else:
        return render_template('index.html', g=gogn, lengd=len(gogn))

@app.route('/nytt')
def nytt():
    return render_template('nyr.html', f=MyForm())

# Custom villuskilaboð
@app.errorhandler(404)
def smu(error):
    return render_template('error404.html')

if __name__ == '__main__':
    app.run(debug=True)
