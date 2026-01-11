# Trade Pro Backend

## Environment Variables (.env)

```
DB_HOSTNAME=localhost
#DB_PORT=Port
DB_PASSWORD=DatabasePass
DB_NAME=DatabaseName
DB_USERNAME=DatabaseUsername
SECRET_KEY=SecretKey
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Start Project

```bash
source ~/.env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app -- --reload
```


