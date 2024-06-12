from flask import render_template, flash, redirect
from app import boiskowo
from app.forms import LoginForm

@boiskowo.route('/')
@boiskowo.route('/index')
def index():
    title = "Boiskowo"
    username = "Jachu"
    posts = [
        {
            'author' : 'Jachu',
            'body' : 'Siema'
        },
        {
            'author': 'Stachu',
            'body': 'Witam'
        }
    ]
    return render_template('index.html', title=title, username=username, posts=posts)

@boiskowo.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template("login.html", form=form)