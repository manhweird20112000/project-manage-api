from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root_app():
    return { 'message': 'Hello World' }