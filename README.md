# Azure Azurite Python Example

When I was at work, I was trying to get azurite to work locally.
Ran into a bunch of issues getting it running.

```shell
$ mkdir -p "azurite"
$ docker-compose up -d azurite
$ pipenv lock
$ pipenv shell
$ ./main.py
```