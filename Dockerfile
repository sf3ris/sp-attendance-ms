FROM python:3.7

WORKDIR /usr/src/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN ls -la

RUN ls -a
#CMD [ "python", "./app/main.py" ]