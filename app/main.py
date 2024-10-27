import uvicorn
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.api.main import api_router
from app.core.secret.config import settings
from app.core.validations.utils import format_validation_errors

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


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print()
    return JSONResponse(
        content=jsonable_encoder(
            {
                "errors": None,
                "data": exc.detail['data'],
                "status_code": exc.status_code,
                "msg":  exc.detail['msg']
            }
        ),
        status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {
                "errors": format_validation_errors(exc.errors()),
                "data": False,
                "status_code": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "msg": "入力データが正しくありません。もう一度お試しください。"
            }
        ),
    )


@app.get('/')
def root_app():
    return { 'message': 'Hello World' }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8888)


