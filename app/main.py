import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.main import api_router
from app.core.secret.config import settings

app = FastAPI()

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')
app.include_router(api_router, prefix=settings.API_V1_STR)
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root_app():
    return { 'message': 'Hello World' }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8888)


