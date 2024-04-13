# influxdb-graphql-bridge
Graph QL server that queries influxdb 

To run:

1. Create a .env file, ensure it is in .gitignore
2. Create and activate python venv from requirements.txt
3. Generate a secret key: python generate_secret_key.py
4. To .env add: SECRET_KEY=<YOUR_SECRET_KEY> (used in settings.py)
3. python manage.py runserver
