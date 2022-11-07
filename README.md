### Run application

Development:

```
> cd src
> python main.py runserver --settings=settings_dev
```

Production:

```
> cd src
> gunicorn main --env DJANGO_SETTINGS_MODULE=settings_prod
```
