from flask import Flask
from flask_migrate import Migrate
from models import db, Workout, Exercise, WorkoutExercises

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/workouts', methods=['GET'])
def get_workouts():
  return("Gotten all workouts")

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
  return(f"Gotten workout with the id: {id}.")

@app.route('/workouts', methods=['POST'])
def create_workout():
  return("Created workout")

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
  return(f"Deleted workout with the id: {id}")

@app.route('/exercises', methods=['GET'])
def get_exercises():
  return("Gotten all exercises")

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercises(id):
  return(f"Gotten exercise with id: {id}")

@app.route('/exercises', methods=['POST'])
def get_exercises():
  return("Created exercise")

@app.route('/exercises/<int:id>', methods=['DELETE'])
def get_exercises():
  return("Gotten all exercises")

@app.route('workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
  return(f"Added exercise with id: {exercise_id} to workout with id: {workout_id}")