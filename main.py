from fastapi import FastAPI


# app object of fast api to define for fastapi
app = FastAPI()

@app.get("/")
def hello():
    return {'message': 'hello world'}

    # another endpoint

@app.get("/about")
def about():
    return {'message': 'Tanmay Mishra is the best'}
