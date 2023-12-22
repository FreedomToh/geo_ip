FROM python:3.11-slim

COPY ./app /app
COPY requirements.txt /app/

RUN apt-get update && pip install --upgrade pip && apt-get install wget -y && apt-get install unzip -y \
    && wget -O - https://github.com/chrislim2888/IP2Location-Python/archive/master.zip > master.zip && unzip master.zip \
    && cd ./IP2Location-Python-master && python3 setup.py build && python3 setup.py install

WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]