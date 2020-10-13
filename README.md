# Match Game

## Prerequisites to Install

* [Python 3.8](https://www.python.org/downloads/)
* [Django 3.1](https://www.djangoproject.com/download/)
* [Channels 2.4](https://channels.readthedocs.io/en/latest/installation.html)
* [Docker](https://www.docker.com/get-started)

## How to Run

```
$ docker run -p 6379:6379 -d redis:5
```

```
$ python3 manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 11, 2020 - 22:53:20
Django version 3.1.2, using settings 'matchgame.settings'
Starting ASGI/Channels version 2.4.0 development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## References

* [Django Tutorial (Polls App)](https://docs.djangoproject.com/en/3.1/intro/tutorial01/)
* [Channels Tutorial (Chat Server)](https://channels.readthedocs.io/en/latest/tutorial/part_1.html)
