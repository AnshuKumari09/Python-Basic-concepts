from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"this is my home"}

@app.get("/anshu")
def myName():
    return {"name":"hello anshu"}

#Route parameter

@app.get("/user/{name}")
def power(name):
    return {"user":name}

@app.get("/search")
def money(item):
    return {"item":item}