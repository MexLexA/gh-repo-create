FROM python:3.8.6-buster


#COPY model.joblib /model.joblib

COPY requirements.txt/ requirements.txt
COPY neurological-roots-of-aesthetics-and-art /neurological-roots-of-aesthetics-and-art
COPY 

#upgrade pip
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["echo", "Hello teammates this is the dcgan image template!"]


#CMD uvicorn api.fast:app --host 0.0.0.0

#CMD uvicorn api.fast:app --host 0.0.0.0 --port $PQRT
