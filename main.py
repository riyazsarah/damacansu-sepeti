from fastapi import FastAPI
import uvicorn
from api.newapp import new_app

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run(new_app(), host="127.0.0.1", port=8080)
