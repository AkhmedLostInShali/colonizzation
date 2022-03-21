from flask_restful import reqparse


class JobsParser(reqparse.RequestParser):
    def __init__(self):
        super().__init__()
        self.add_argument('id', required=True, type=int)
        self.add_argument('job', required=True)
        self.add_argument('work_size', required=True, type=int)
        self.add_argument('collaborators', required=True)
        self.add_argument('is_finished', required=True, type=bool)
        self.add_argument('team_leader', required=True, type=int)


class UserParser(reqparse.RequestParser):
    def __init__(self):
        super().__init__()
        self.add_argument('id', required=True, type=int)
        self.add_argument('email', required=True)
        self.add_argument('password', required=True)
        self.add_argument('password_again', required=True)
        self.add_argument('surname', required=True)
        self.add_argument('name', required=True)
        self.add_argument('age', required=True, type=int)
        self.add_argument('position', required=True)
        self.add_argument('speciality', required=True)
        self.add_argument('address', required=True)
        self.add_argument('city_from', required=True)

        'email', 'surname', 'name', 'age', 'position', 'speciality', 'address',
        'password', 'password_again', 'city_from'