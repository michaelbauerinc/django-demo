# django-demo
A small demo app made with Django

## Installation

1) Clone the repo

2) Fill out environment variables based on env.sh template.

3) Start the app

```bash
sh start.sh
```


## To salt db with posts (TODO: to refactor into one script):
```bash
- create two new users
- python manage.py shell
- exec(open('./utils/add_posts.py').read())
```

## Dependencies

1) Docker
