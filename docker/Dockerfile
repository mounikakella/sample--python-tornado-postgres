FROM python:3.9

WORKDIR /opt/app

RUN pip3 install pipenv

COPY Pipfile .

RUN pipenv install

COPY . .

ENV DATABASE=postgres \
    HOST=localhost \
    USER=postgres \
    PASSWORD=postgres

ENTRYPOINT [ "pipenv", "run", "python3", "app.py" ]