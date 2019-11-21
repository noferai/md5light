import os
import hashlib
from celery import Celery
from urllib.request import urlopen
from utils import notify

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)


@celery.task(name='tasks.get_remote_hash')
def get_remote_hash(**kwargs):
    md5_hash = hashlib.md5()
    with urlopen(kwargs['url']) as request:
        for chunk in iter(lambda: request.read(4096), b''):
            md5_hash.update(chunk)
    md5 = str(md5_hash.hexdigest())
    if 'email' in kwargs.keys():
        notify(email=str(kwargs['email']), text=('File: ' + kwargs['url'] + ' | ' + 'MD5: ' + md5))
    return md5, kwargs['url']

