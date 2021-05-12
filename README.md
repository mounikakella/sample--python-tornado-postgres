# sample--python-tornado-postgres

## TO RUN:
```
docker run -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -e POSTGRES_USER=postgres postgres:latest
```
```
pipenv install
export HOST=localhost   
export PORT=5432
export DATABASE=postgres     
export USER=postgres    
export PASSWORD=postgres
pipenv run python app.py
```
