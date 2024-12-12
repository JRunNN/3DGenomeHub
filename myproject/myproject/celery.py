import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

#  celery -A backend worker --loglevel=info -P gevent --concurrency 1 -E
# app = Celery("myproject", broker='redis://:sad*$ds@Asd9@redis:6379/0', backend='redis://:sad*$ds@Asd9@redis:6379/0')
app = Celery("myproject",broker='redis://47.107.91.5:6379/0', backend='redis://47.107.91.5:6379/0')
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')