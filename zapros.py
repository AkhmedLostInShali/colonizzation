from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.departments import Department
from data.users import User

global_init('db/mars_explorer.db')
db_sess = create_session()
department = db_sess.query(Department).filter(Department.id == 1).first()
department_workers = [int(x) for x in department.members.split(', ')]
all_jobs = db_sess.query(Jobs).all()
hours = dict()
for worker in department_workers:
    time = 0
    for job in all_jobs:
        if worker in set([job.team_leader] + [int(x) for x in job.collaborators.split(', ')]):
            time += job.work_size
    teamleader = db_sess.query(User).filter(User.id == worker).first()
    name = teamleader.surname + ' ' + teamleader.name
    if name in hours:
        hours[name] += time
    else:
        hours[name] = time
for name, time in hours.items():
    if time > 25:
        print(name)
