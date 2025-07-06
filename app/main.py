from fastapi import FastAPI, Query
from app import operations

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Calculator is live!"}

@app.get("/add")
def add(a: float = Query(...), b: float = Query(...)):
    return {"result": operations.add(a, b)}

@app.get("/subtract")
def subtract(a: float = Query(...), b: float = Query(...)):
    return {"result": operations.subtract(a, b)}

@app.get("/multiply")
def multiply(a: float = Query(...), b: float = Query(...)):
    return {"result": operations.multiply(a, b)}

@app.get("/divide")
def divide(a: float = Query(...), b: float = Query(...)):
    try:
        return {"result": operations.divide(a, b)}
    except ValueError as e:
        return {"error": str(e)}

