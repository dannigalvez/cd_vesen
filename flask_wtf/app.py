from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired 

jon = Flask(__name__)
jon.config['SECRET_KEY'] = "Nú er gaman" # ÞETTA ÞARF AÐ VERA LEYNILEGT...

class LoginForm(FlaskForm):
    notendanafn = StringField("Notendanafn:", validators=[InputRequired()])
    lykilord = PasswordField("Lykilorð:", validators=[InputRequired()])
    prufa = StringField("Prufa:", validators=[InputRequired()])
    hnappur = SubmitField("Innskrá")

@jon.route('/')
def index():
    return render_template("index.html", lf = LoginForm() )

@jon.route('/login', methods=["POST","Get"])
def login():
    lf = LoginForm()
    if request.form:
        n = lf.notendanafn.data
        l = lf.lykilord.data
        p = request.form.get("prufa")
        print(lf.data)
        
        return render_template("gogn.html", n=n,l=l,p=p)
    else: 
        return "Má ekki..."

if __name__ == "__main__":
    jon.run(debug=True)