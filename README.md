# sample--python-tornado-postgres

## TO RUN:
```
docker run -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -e POSTGRES_USER=postgres postgres:latest
```
```
pipenv install
export DATABASE=postgres     
export USER=postgres    
export PORT=5432        
pipenv run python app.py
```
