from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# The schema is used for validation and serialization and deserialization
# Load is essentially used when saving/creating data and dumps is used to get data
# Routes - serialization -> dumps(Object to JSON), deserialization -> loads(JSON to Object)
@app.route('/workouts', methods=['GET'])
def get_workouts():
  workouts = Workout.query.all() # Get all workout data
  schema = WorkoutSchema(many=True) # When serializing a collection of objects
  return make_response(jsonify(schema.dump(workouts)), 200)

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
  workout = Workout.query.get_or_404(id) # Either displays the data or shows data not found
  schema = WorkoutSchema() # When serializing one object
  return make_response(jsonify(schema.dump(workout)), 200)

@app.route('/workouts', methods=['POST'])
def create_workout():
  schema = WorkoutSchema() 
  try:
      data = schema.load(request.json) # Recieves JSON data sent and changes it to a python object after validation
  except ValidationError as err:
      return jsonify(err.messages), 400

  workout = Workout(**data)
  db.session.add(workout)
  db.session.commit()
  return make_response(jsonify(schema.dump(workout)), 201)

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
  workout = Workout.query.get_or_404(id) 
  db.session.delete(workout)
  db.session.commit() # Save changes to database
  return jsonify({"message": f"Deleted workout with id {id}"}), 200

@app.route('/exercises', methods=['GET'])
def get_exercises():
  exercises = Exercise.query.all()
  schema = ExerciseSchema(many=True)
  return jsonify(schema.dump(exercises))

@app.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
  exercise = Exercise.query.get_or_404(id) 
  schema = ExerciseSchema() 
  return make_response(jsonify(schema.dump(exercise)), 200)

@app.route('/exercises', methods=['POST'])
def create_exercises():
  schema = ExerciseSchema()
  try:
      data = schema.load(request.json)
  except ValidationError as err:
      return make_response(jsonify(err.messages), 400)

  exercise = Exercise(**data)
  db.session.add(exercise)
  db.session.commit()
  return make_response(jsonify(schema.dump(exercise)), 201)

@app.route('/exercises/<int:id>', methods=['DELETE'])
def delete_exercises():
  exercise = Exercise.query.get_or_404(id) 
  db.session.delete(exercise)
  db.session.commit() 
  return jsonify({"message": f"Deleted exercise with id {id}"}), 200

@app.route('/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises', methods=['POST'])
def add_exercise_to_workout(workout_id, exercise_id):
  schema = WorkoutExercisesSchema()
  try:
      data = schema.load(request.json)
  except ValidationError as err:
      return jsonify(err.messages), 400
  workout_exercise = WorkoutExercises(workout_id=workout_id, exercise_id=exercise_id, **data)
  db.session.add(workout_exercise)
  db.session.commit()
  return jsonify(schema.dump(workout_exercise)), 201

if __name__ == '__main__':
  app.run(port=5555, debug=True)