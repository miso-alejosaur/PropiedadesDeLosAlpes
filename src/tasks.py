#Example

from tasks import Celery

app = Celery('tasks', broker='redis://broker:6379', backend='redis://broker:6379')

@app.task
def add(x, y):
    return x + y

#add.delay(10, 10)
#poetry run celery -A src.tasks worker -l INFO