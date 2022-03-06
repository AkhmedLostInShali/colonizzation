from data import db_session, users, jobs
from flask import Flask, url_for, redirect, render_template, request, session
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    app.run(port=8080, host='127.0.0.1')


@app.route('/')
def first_table():
    session = db_session.create_session()
    stuff = session.query(users.User).all()
    work_list = session.query(jobs.Jobs).all()
    return render_template('user_job_table.html', team=stuff, works=work_list)


if __name__ == '__main__':
    main()