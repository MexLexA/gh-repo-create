from fastapi import FastAPI
#from fastapi.middleware.cors import CORSMiddleware
#import random
#import os


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

@app.get("/")
def index():
    return {"docker-status": "WHERES DA TUOLET MATE!!!"}


# @app.get("/art")
# def art():
#    stream = os.popen('python generator.py generate-latent-walk --network="{explored_network}--outdir="{latent_walk_path}" --trunc=0.7 --walk-type="{walk_types[2]}" \
#       --seeds={','.join(map(str, seeds))} --frames {len(seeds)*20}')
#    output = stream.read()

#    print(output)
