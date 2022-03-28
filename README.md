# dam-operation-model
## Prerequisite
- Docker
- Python 3.9 can be used alternatively

## Components
- src : main dam model
- inp : input csv file
- out : output csv file
- tool : utils

## How to run
1. Navigate to `dam-operation-model/`
2. Build:
    - `docker compose up -d --build`
3. Confirm the image and the container is up:
    - `docker image ls`
    - `docker container ls`
3. Connect to the container:
    - `docker compose exec python3 bash`