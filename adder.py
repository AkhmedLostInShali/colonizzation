from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    job = Jobs()
    job.team_leader = 3
    job.job = 'Set an auto-pilot'
    job.work_size = 48
    job.collaborators = '4, 2, 1'
    job.is_finished = False
    db_sess = db_session.create_session()
    db_sess.add(job)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
