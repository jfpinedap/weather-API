
# Code Challenge

This API provide by city the current weather data and forecast for next 7 days.


## Requisites

* Git
* Docker
* Docker-compose
* .local → file with local environment variables **provided by email**
## How to use this project

* Clone this repository
  ```sh
  git clone https://github.com/jfpinedap/weather-api.git
  ```

* Copy .local file in .envs folder

* Build the Dockerfile
  ```sh
  docker-compose up --build -d
  ```

* Request localy by port 8000
  ```sh
  http://0.0.0.0:8000/weather?city=lima&country=pe
  ```

* Testing
  ```sh
  docker-compose run --rm django python manage.py test
  ```


## Documentation

Postman Documentation [Documentation Postman](https://documenter.getpostman.com/view/14155075/TVzUEGtt "Postman Doc")

## Used technologies

* Django
* Django Rest Framework
* Redis
* [Docker](https://www.docker.com/ "Docker link")
* Docker-compose

## Licence

GNU-GPL 3.0
