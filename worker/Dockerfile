FROM python:3.8-alpine

WORKDIR /code

# Install python/pip

RUN pip3 install -r requirements.txt

COPY . /code

CMD ["python3", "/code/server.py"]
