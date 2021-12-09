from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import os


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index():
    return {"docker-status": "WHERES DA TUOLET MATE!!!"}


@app.get("/art")
def art():
   stream = os.popen('python3 generate.py --trunc=1 --seeds=85,265,297,849 \
    --outdir="out" --network=https://nvlabs-fi-cdn.nvidia.com/stylegan2-ada/pretrained/metfaces.pkl')
   output = stream.read()

   print(output)
