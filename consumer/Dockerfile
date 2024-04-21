FROM python:3.10-alpine3.18

WORKDIR /workdir

COPY requirements.txt /workdir/requirements.txt

RUN  pip install --upgrade pip ;\
     pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /workdir

CMD ["python", "-u", "main.py"]