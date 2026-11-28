
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Jenkins CI/CD Application"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}
