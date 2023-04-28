from django_celery_beat.models import IntervalSchedule, PeriodicTask

import json

def schedule_setup():
    minute_schedule, created = IntervalSchedule.objects.get_or_create(period=IntervalSchedule.MINUTES,every=1)

    args = json.dumps(["python"])

    pt = PeriodicTask.objects.create(
    name="Notifier",
    interval=minute_schedule,
    args=args,
    task="movies.tasks.notify_of_starting_soon"
)
