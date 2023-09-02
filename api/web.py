from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Form
import uvicorn

templates_home = Jinja2Templates(directory="../home")
templates_zoom = Jinja2Templates(directory="../djzoom")
templates_reg = Jinja2Templates(directory="../register")
templates_login = Jinja2Templates(directory="../login")
templates_logout = Jinja2Templates(directory="../logout")

app = FastAPI(docs_url="/docs", redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def home(request: Request):
    return templates_home.TemplateResponse("index.html",{"request":request})

@app.get("/djzoom")
async def djzoom(request: Request):
    return templates_zoom.TemplateResponse("index.html",{"request":request})

@app.get("/register")
async def register(request: Request):
    return templates_reg.TemplateResponse("index.html",{"request":request})

@app.post("/signup")
async def signup(request: Request, username: str = Form(...), password: str = Form(...)):
    # 이 부분을 DB로 전송
    
    return "signup Successful"

@app.get("/login")
async def login(request: Request):
    return templates_login.TemplateResponse("index.html",{"request":request})

@app.get("/logout")
async def logout(request: Request):
    msg = "logout Successful"
    response = templates_logout.TemplateResponse("login.html", {"request":request, "msg":msg})
    response.delete_cookie(key="access_token")
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)