## Heroku Commands
- Heroku Logs: `heroku logs -a mine-demo --tail`   
- Heroku Reset: `heroku ps:restart -a mine-demo`
- Heroku Migrate: `heroku run python manage.py migrate -a mine-demo`
- Heroku Access DB: `heroku pg:psql -a mine-demo` | `SELECT * FROM "MiningData";`
- Clear the database: `heroku pg:reset DATABASE_URL --app your-app-name`


## Local Commands: 
- `python manage.py makemigrations api`
- `python manage.py migrate`
- `venv\Scripts\activate`

## Python Commands: 
- Print MiningData Table Data: `python manage.py print_db_data`
- Clear MiningData Table Data: `python manage.py clear_db_data`
- Add new entry to MiningData: `python manage.py new_bucket`




PROJECT DIR:

MS-DEMO
| - api
| | - management
| | | - commands
| | | | - clear_db_data.py
| | | | - get_data.py
| | - migrations
| | - templates
| | | - index.html 
| | - __init__.py
| | - admin.py
| | - apps.py
| | - models.py
| | - tests.py
| | - views.py 
| - djangoapp
| | - __pycache__/
| | - __init__.py
| | - asgi.py
| | - settings.py
| | - urls.py
| | - wsgi.py
| - reactapp
| - static
| | - build
| | | - static
| | | - asset-manifest.json
| | | - favicon.ico
| | | - index.html
| | | - logo192.png
| | | - logo512.png
| | | - manifest.json
| | | - robots.txt
| - staticfiles
| - venv
| - .env
| - .gitignore
| - manage.py
| - Procfile
| - README.md
| - requirements.txt
| - update-app.bat 
