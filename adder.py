from flask import Flask
from data import db_session
from data.jobs import Jobs
from data.departments import Department

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    dep = Department()
    dep.chief = 3
    dep.title = 'geological exploration'
    dep.work_size = 48
    dep.members = '4, 2, 1'
    dep.email = 'geological@email.cu'
    db_sess = db_session.create_session()
    db_sess.add(dep)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
