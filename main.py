from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
import uvicorn

from api import routes

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(routes.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=3000, reload=True, access_log=False)
