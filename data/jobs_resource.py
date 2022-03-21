from flask import jsonify, request
from flask_restful import abort, Resource
from . import db_session, my_parsers
from .jobs import Jobs

parser = my_parsers.JobsParser()


def abort_if_jobs_not_found(jobs_id):
    session = db_session.create_session()
    news = session.query(Jobs).get(jobs_id)
    if not news:
        abort(404, message=f"Jobs {jobs_id} not found")


class JobsResource(Resource):
    def get(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(jobs_id)
        return jsonify(
            {
                'news': job.to_dict(only=(
                    'id', 'job', 'user.name', 'is_finished', 'collaborators'))
            }
        )

    def delete(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        db_sess = db_session.create_session()
        job = db_sess.query(Jobs).get(jobs_id)
        db_sess.delete(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})

    def put(self, jobs_id):
        abort_if_jobs_not_found(jobs_id)
        db_sess = db_session.create_session()
        if request.json.get('id') and request.json.get('id') in [job.id for job in db_sess.query(Jobs).all()]:
            return jsonify({'error': ' Id already exists'})
        job = db_sess.query(Jobs).get(jobs_id)
        job.id = request.json['id'] if request.json.get('id') else job.id
        job.job = request.json['job'] if request.json.get('job') else job.job
        job.team_leader = request.json['team_leader'] if request.json.get('team_leader') else job.team_leader
        job.work_size = request.json['work_size'] if request.json.get('work_size') else job.work_size
        job.start_date = request.json['start_date'] if request.json.get('start_date') else job.start_date
        job.end_date = request.json['end_date'] if request.json.get('end_date') else job.end_date
        job.collaborators = request.json['collaborators'] if request.json.get('collaborators') else job.collaborators
        job.is_finished = (request.json['is_finished']
                           if request.json.get('is_finished') is not None else job.is_finished)
        db_sess.commit()
        return jsonify({'success': 'OK'})


class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(Jobs).all()
        return jsonify({
            'news':
                [item.to_dict(only=('id', 'job', 'work_size', 'collaborators', 'team_leader', 'is_finished',
                                    'start_date')) for item in news]})

    def post(self):
        args = parser.parse_args()
        db_sess = db_session.create_session()
        if request.json.get('id') and request.json.get('id') in [job.id for job in db_sess.query(Jobs).all()]:
            return jsonify({'error': ' Id already exists'})
        job = Jobs()
        if args.get('id'):
            job.id = args.get('id')
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.is_finished = args['is_finished']
        job.team_leader = args['team_leader']

        db_sess.add(job)
        db_sess.commit()
        return jsonify({'success': 'OK'})
