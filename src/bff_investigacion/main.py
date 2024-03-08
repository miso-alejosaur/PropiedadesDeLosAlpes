import asyncio
from fastapi import FastAPI

from consumidores import suscribirse_a_topico

app = FastAPI()
tasks = list()
eventos = list()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def app_startup():
    global tasks
    global eventos
    task1 = asyncio.ensure_future(suscribirse_a_topico("eventos-puntaje", eventos=eventos))
    tasks.append(task1)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()