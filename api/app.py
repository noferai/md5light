from flask import Flask, request, jsonify
from worker import celery
import celery.states as states

app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    task = celery.send_task('tasks.get_remote_hash', kwargs=request.args.to_dict())
    return jsonify({'id': task.id})


@app.route('/check', methods=['GET'])
def check():
    res = celery.AsyncResult(request.args.get('id'))
    if res.state == states.PENDING:
        return 'task not found', 404
    if res.state == states.FAILURE:
        return 'error', 500
    elif res.state == states.STARTED:
        return jsonify({'status': res.state})
    else:
        return jsonify({'md5': res.result[0], 'status': res.state, 'url': res.result[1]})
