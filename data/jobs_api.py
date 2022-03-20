from flask import jsonify, Blueprint, request
from . import db_session
from .jobs import Jobs

blueprint = Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'news':
                [item.to_dict(only=('id', 'job', 'work_size', 'collaborators', 'team_leader', 'is_finished',
                                    'start_date'))
                 for item in news]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_job(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'news': job.to_dict(only=(
                'id', 'job', 'user.name', 'is_finished', 'collaborators'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['job', 'work_size', 'collaborators', 'is_finished', 'team_leader']):
        return jsonify({'error': 'Bad request'})
    db_sess = db_session.create_session()
    if request.json.get('id') and request.json.get('id') in [job.id for job in db_sess.query(Jobs).all()]:
        return jsonify({'error': ' Id already exists'})
    job = Jobs()
    if request.json.get('id'):
        job.id = request.json.get('id')
    job.job = request.json['job']
    job.work_size = request.json['work_size']
    job.collaborators = request.json['collaborators']
    job.is_finished = request.json['is_finished']
    job.team_leader = request.json['team_leader']

    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['DELETE'])
def delete_job(jobs_id):
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    db_sess.delete(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['PUT'])
def redact_job(jobs_id):
    if not request.json:
        return jsonify({'error': 'Empty request'})
    db_sess = db_session.create_session()
    if request.json.get('id') and request.json.get('id') in [job.id for job in db_sess.query(Jobs).all()]:
        return jsonify({'error': ' Id already exists'})
    job = db_sess.query(Jobs).get(jobs_id)
    if not job:
        return jsonify({'error': 'Not found'})
    job.id = request.json['id'] if request.json.get('id') else job.id
    job.job = request.json['job'] if request.json.get('job') else job.job
    job.team_leader = request.json['team_leader'] if request.json.get('team_leader') else job.team_leader
    job.work_size = request.json['work_size'] if request.json.get('work_size') else job.work_size
    job.start_date = request.json['start_date'] if request.json.get('start_date') else job.start_date
    job.end_date = request.json['end_date'] if request.json.get('end_date') else job.end_date
    job.collaborators = request.json['collaborators'] if request.json.get('collaborators') else job.collaborators
    job.is_finished = request.json['is_finished'] if request.json.get('is_finished') is not None else job.is_finished
    db_sess.commit()
    return jsonify({'success': 'OK'})
