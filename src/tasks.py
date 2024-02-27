#Example

from celery import Celery

app = Celery('tasks',
            broker='redis://broker:6379',
            include=['src.example.tasks', 'src.pda.modulos.transacciones.aplicacion.servicios']
            )

@app.task
def add(x, y):
    print(f"{x}+{y}={x+y}")
    return x + y

#add.delay(10, 10)
#poetry run celery -A src.tasks worker -l INFO