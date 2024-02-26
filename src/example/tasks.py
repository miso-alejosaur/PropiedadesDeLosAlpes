from src.tasks import app

@app.task
def multiplication(x, y):
    print(f"{x}*{y}={x*y}")
    return x * y