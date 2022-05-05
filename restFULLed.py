import json
from random import choice

from data import db_session, jobs_api, users_api, jobs_resource, users_resource
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from flask import Flask, render_template, redirect, request, abort
from forms.jobform import JobForm
from forms.registerform import RegisterForm
from forms.loginform import LoginForm
from forms.departmentform import DepartmentForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_restful import reqparse, Api, Resource
from requests import get

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/mars_explorer.db")
    api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
    api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:jobs_id>')
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')
    app.register_blueprint(jobs_api.blueprint)
    app.register_blueprint(users_api.blueprint)
    app.run(port=8080, host='127.0.0.1')


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/')
@app.route('/jobs')
def job_table():
    session = db_session.create_session()
    stuff = session.query(User).all()
    work_list = session.query(Jobs).all()
    return render_template('job_table.html', title='Таблица работ', team=stuff, works=work_list)


@app.route('/departments')
def dep_table():
    session = db_session.create_session()
    stuff = session.query(User).all()
    dep_list = session.query(Department).all()
    return render_template('dep_table.html', title='Таблица департаментов', team=stuff, departments=dep_list)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User()
        user.name = form.name.data
        user.email = form.email.data
        user.surname = form.surname.data
        user.age = form.age.data
        user.position = form.position.data
        user.speciality = form.speciality.data
        user.address = form.address.data
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/job', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        job = Jobs()
        job.job = form.job_title.data
        job.work_size = form.work_size.data
        job.collaborators = form.collaborators.data
        job.is_finished = form.is_finished.data
        job.team_leader = current_user.id
        db_sess = db_session.create_session()
        db_sess.merge(current_user)
        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('add_job.html', title='Добавление работы', form=form, leader=current_user.id)


@app.route('/department', methods=['GET', 'POST'])
@login_required
def add_dep():
    form = DepartmentForm()
    if form.validate_on_submit():
        dep = Department()
        dep.title = form.title.data
        dep.email = form.email.data
        dep.members = form.members.data
        dep.chief = current_user.id
        db_sess = db_session.create_session()
        db_sess.merge(current_user)
        db_sess.add(dep)
        db_sess.commit()
        return redirect('/departments')
    return render_template('add_dep.html', title='Добавление работы', form=form, leader=current_user.id)


@app.route('/edit_job/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_job(id):
    form = JobForm()
    lead_id = "-"
    if request.method == "GET":
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if job and current_user.id in [job.team_leader, 1]:
            form.job_title.data = job.job
            form.work_size.data = job.work_size
            form.collaborators.data = job.collaborators
            form.is_finished.data = job.is_finished
            lead_id = job.team_leader
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).filter(Jobs.id == id).first()
        if job and current_user.id in [job.team_leader, 1]:
            job.job = form.job_title.data
            job.team_leader = form.team_leader.data
            job.work_size = form.work_size.data
            job.collaborators = form.collaborators.data
            job.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('add_job.html', title='Изменение работы', form=form, leader=lead_id)


@app.route('/edit_department/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_dep(id):
    form = DepartmentForm()
    lead_id = "-"
    if request.method == "GET":
        db_sess = db_session.create_session()
        dep = db_sess.query(Department).filter(Department.id == id).first()
        if dep and current_user.id in [dep.chief, 1]:
            form.title.data = dep.title
            form.email.data = dep.email
            form.members.data = dep.members
            lead_id = dep.chief
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        dep = db_sess.query(Department).filter(Department.id == id).first()
        if dep and current_user.id in [dep.chief, 1]:
            dep.title = form.title.data
            dep.chief = form.chief.data
            dep.email = form.email.data
            dep.members = form.members.data
            db_sess.commit()
            return redirect('/departments')
        else:
            abort(404)
    return render_template('add_dep.html', title='Изменение департамента', form=form, leader=lead_id)


@app.route('/delete_job/<int:id>', methods=['GET', 'POST'])
@login_required
def job_delete(id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if job and current_user.id in [job.team_leader, 1]:
        db_sess.delete(job)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/delete_department/<int:id>', methods=['GET', 'POST'])
@login_required
def dep_delete(id):
    db_sess = db_session.create_session()
    dep = db_sess.query(Department).filter(Department.id == id).first()
    if dep and current_user.id in [dep.chief, 1]:
        db_sess.delete(dep)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/departments')


@app.route('/users_show/<int:users_id>', methods=['GET'])
def show_city(users_id):
    user = get(f'http://localhost:8080/api/users/{users_id}').json()['user']
    print(user)
    if not user.get('city_from'):
        abort(404)
    json_response = get("http://geocode-maps.yandex.ru/1.x/?apikey="
                        + f"40d1649f-0493-4b70-98ba-98533de7710b&geocode={user.get('city_from')}&format=json").json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    coordinates = ','.join(toponym["Point"]["pos"].split(' '))
    img_src = f"http://static-maps.yandex.ru/1.x/?ll={coordinates}&l=sat&z=12"
    return render_template('show_city.html', name=user.get('name'), surname=user.get('surname'), img_src=img_src)


@app.route('/member')
def random_member():
    with open('templates/members.json') as f:
        member_data = choice(json.load(f))
    return render_template('member.html', member=member_data)


if __name__ == '__main__':
    main()