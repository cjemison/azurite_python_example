# Azure Azurite Python Example

When I was at work I was trying to get Azurite to work locally, I Ran into a bunch of issues getting it running.

```shell
$ mkdir -p "azurite"
$ docker-compose up -d azurite
$ pipenv --python 3.9.2
$ pipenv install
$ pipenv shell
$ ./main.py
$ pipenv --rm # deletes the virtualenv
```