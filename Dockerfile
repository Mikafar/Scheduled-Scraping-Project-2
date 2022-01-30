FROM  python:3.10.2-bullseye
RUN pip install --upgrade pip
COPY vital-folder-331713-15f519e71cc2.json vital-folder-331713-15f519e71cc2.json
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt