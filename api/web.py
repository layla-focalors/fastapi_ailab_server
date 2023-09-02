from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

templates_home = Jinja2Templates(directory="../home")
templates_zoom = Jinja2Templates(directory="../djzoom")
templates_reg = Jinja2Templates(directory="../register")
templates_login = Jinja2Templates(directory="../login")

app = FastAPI(docs_url="/docs", redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def home(request: Request):
    return templates_home.TemplateResponse("index.html",{"request":request})

@app.get("/djzoom")
async def djzoom(request: Request):
    return templates_zoom.TemplateResponse("index.html",{"request":request})

@app.get("/register")
async def register(request: Request):
    return templates_reg.TemplateResponse("index.html",{"request":request})

@app.get("/login")
async def login(request: Request):
    return templates_login.TemplateResponse("index.html",{"request":request})

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)