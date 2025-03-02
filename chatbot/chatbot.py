from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configurar CORS para permitir solicitudes desde el frontend (puerto 8080)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia "*" por ["http://127.0.0.1:8080"] si quieres restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo de datos para recibir mensajes
class Mensaje(BaseModel):
    mensaje: str

@app.post("/chat")
async def responder(mensaje: Mensaje):
    respuesta = f"Recibí tu mensaje: {mensaje.mensaje}"
    return {"respuesta": respuesta}

# Ejecutar el servidor con:
# uvicorn chatbot:app --reload
