  ~~Introduction~~
> This is a project made using Python as a main programming language with the help of flask, flask_sqlalchemy, marshmallow and flask_migrate.
> It is a workout app that showcases various workouts and exercises.

 ~~Installation~~
> Run pipenv install and pipenv shell to install all dependencies and enter a virtual environment.
> To check the version of the dependencies on you PC type pip show <dependency_name> without the <> and update the pipfile accordingly.

  ~~Seeding~~
> Run python3 seed.py to seed the database since you shouldn't push databases to github

  ~~Testing API endpoints using Postman~~
> Start the server by running python3 app.py in the terminal
> To Get data, paste the http link on your browser and select GET.
> To Post data, select POST and in headers, set the key as: Content-Type and the value as: application/json in the body, select the raw and paste your JSON data there then send.
> Here's an example of test data for the /workouts endpoint:
{
  "date": "2026-07-25",
  "duration_minutes": 45,
  "notes": "Evening cardio session"
}
> Here's an example of test data for the /exercises endpoint:
{
  "name": "Bench Press",
  "category": "Arms",
  "equipment_needed": true
}
> To Delete data type in the endpoint URL with the ID and select DELETE and send



