source .env
docker build -t optimy-app src/php/
docker tag optimy-app:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/optimy-app:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/optimy-app:latest

docker build -t optimy-db src/mysql/
docker tag optimy-db:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/optimy-db:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/optimy-db:latest

docker build -t optimy-testing src/testing/
docker tag optimy-testing:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/optimy-testing:latest
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/optimy-testing:latest