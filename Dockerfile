FROM  python:3.10.2-bullseye
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt