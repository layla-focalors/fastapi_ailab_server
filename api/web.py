from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Form
from loginsys import login
from rank import rank
from skills import skills
from connect import connect
import uvicorn

templates_home = Jinja2Templates(directory="../home")
templates_zoom = Jinja2Templates(directory="../djzoom")
templates_reg = Jinja2Templates(directory="../register")
templates_login = Jinja2Templates(directory="../login")
templates_logout = Jinja2Templates(directory="../logout")

visit_count = 0

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
    await connect("register", username, password)
    return "signup Successful"

@app.get("/login")
async def signup(request: Request, username: str = Form(...),password: str = Form(...)):
    if request.cookies.get("access_token"):
        # access 토큰이 있는 경우
        return templates_login.TemplateResponse("index.html",{"request":request})
    if await login("login", username, password) == True:
        return templates_login.TemplateResponse("index.html",{"request":request})
    else:
        return "login Failed"

@app.post("/signin")
async def signin(request: Request, username: str = Form(...), password: str = Form(...)):
    import uuid
    # await connect("login", username, password)
    response = templates_login.TemplateResponse("login.html", {"request":request})
    response.set_cookie(key="access_token", value=f"{uuid.uuid4()}", httponly=True)
    return response

@app.get("/visitor")
async def visitor(request: Request):
    return visit_count

@app.get("/ranking")
async def ranking(request: Request):
    df = rank()
    return df

@app.get("/ranking/{user}")
async def ranking(request: Request, user: str):
    df = rank(user)
    return df

@app.get("/skills/{user}")
async def skills(request: Request, user: str):
    df = skills(user)
    return df

@app.get("/contact/{user}")
async def contact(request: Request, user: str):
    url = contact(user)
    return str(url)

@app.get("/logout")
async def logout(request: Request):
    msg = "logout Successful"
    response = templates_logout.TemplateResponse("login.html", {"request":request, "msg":msg})
    response.delete_cookie(key="access_token")
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="localhost",port=8000)