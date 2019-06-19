FROM python:3

ADD app.py app.py

ADD config.yaml config.yaml

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]