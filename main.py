from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import RedirectResponse, FileResponse
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# password to unlock
PASSWORD = "123"
# session
app.add_middleware(SessionMiddleware, secret_key="4D13E32A5C7245D7ACA68BA774B42")
# set up static html
app.mount("/static", StaticFiles(directory="static"), name="static")

# remove cache by browser to prevent page not refreshed
@app.middleware("http")
async def no_cache(request, call_next):
    response = await call_next(request)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

async def is_logged_in(request: Request):
    return request.session.get("logged_in") is True
@app.get("/")
async def check_logged_in(response: Response, request: Request):
    if await is_logged_in(request):
        return FileResponse("./static/index.html")
    return FileResponse("./static/login.html")

@app.post("/login")
async def login(request: Request, password: str = Form(...)):
    if password == PASSWORD:
        request.session["logged_in"] = True
        return RedirectResponse("/", status_code=303)
    return {"error": "wrong password"}

@app.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=302)