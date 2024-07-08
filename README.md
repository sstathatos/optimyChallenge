## Welcome to OptimyChallenge!
To run the app locally:
1. Setup a .env file with the following parameters:
```MYSQL_ROOT_PASSWORD=
MYSQL_DATABASE=
DB_HOST=
DB_USER=
DB_PASS=
DB_NAME=
```
2. Run `docker compose up --build`

## Create ECR repos
```
aws ecr create-repository --repository-name optimy-app
aws ecr create-repository --repository-name optimy-db
```

## Deploy images
