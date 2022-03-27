import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portal.settings')

app = Celery('portal')
app.config_from_object('django.conf:settings', namespace='CELERY')
# app.conf.update(
#     beat_scheduler="django_celery_beat.schedulers:DatabaseScheduler",
# )

app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'send_mailing_everyday_8am': {
#         'task': 'board.tasks.do_mailing',
#         'schedule': crontab(minute='*/1'),
#         # 'schedule': crontab(hour=8, minute=0),
#     },
# }
