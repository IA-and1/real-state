from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

# Servir archivos estáticos (CSS, imágenes, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2 para renderizar HTML
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chatbot")
async def chatbot_endpoint(request: Request):
    data = await request.json()
    user_query = data.get("query", "")

    # Respuesta simple (puedes integrar IA aquí)
    response_text = f"🤖 Respuesta: Recibí tu mensaje: '{user_query}'"

    return JSONResponse(content={"response": response_text})
