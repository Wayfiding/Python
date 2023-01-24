from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringFile, SubmitField




app = Flask(__name__)
app.config['SECRTE_KEY'] = 'hard to guess string'

moment = Moment(app)
bootstrap = Bootstrap(app)

def index():
    return render_template('index.html', current_time=datetime.utcnow())
app.add_url_rule('/','index',index)

@app.route('/user/<var1>')
def user(var1):
    return render_template('user.html',name=var1)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

class NameForm(FlaskForm):
    name = StringField('What is your name?',
    validators=[DataRequired()])
    submit = SubmitField('Submit')


