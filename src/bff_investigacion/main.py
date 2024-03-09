from fastapi import FastAPI, Request
import asyncio
import time
import traceback
import uvicorn
import uuid
import datetime

from pydantic import BaseSettings
from typing import Any

from consumidores import suscribirse_a_topico
from api.v1.router import router as v1


from sse_starlette.sse import EventSourceResponse

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
    print(f'aquivoy')
    task1 = asyncio.ensure_future(suscribirse_a_topico("eventos-auditoria-integracion", eventos=eventos))
    tasks.append(task1)

@app.on_event("shutdown")
def shutdown_event():
    global tasks
    for task in tasks:
        task.cancel()

@app.get('/stream')
async def stream_mensajes(request: Request):
    def nuevo_evento()
        global eventos
        return {'data': eventos.pop(), 'event': 'NuevoEvento'}
    async def leer_eventos():
        global eventos
        while True:
            # Si el cliente cierra la conexión deja de enviar eventos
            if await request.is_disconnected():
                break

            if len(eventos) > 0:
                yield nuevo_evento()

            await asyncio.sleep(0.1)

    return EventSourceResponse(leer_eventos())

app.include_router(v1, prefix="/v1")