from data import db_session, jobs_api, jobs_resource
from data.users import User
from data.jobs import Jobs
from data.departments import Department
from flask import Flask, render_template, redirect, request, abort, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from forms.jobform import JobForm
from forms.registerform import RegisterForm
from forms.loginform import LoginForm
from forms.departmentform import DepartmentForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

app = Flask(__name__)
api = Api(app)
# для списка объектов
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')

# для одного объекта
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:jobs_id>')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    db_session.global_init("db/mars_explorer.db")
    app.register_blueprint(jobs_api.blueprint)
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()