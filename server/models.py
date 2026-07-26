from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy import MetaData
metadata = MetaData()
db = SQLAlchemy(metadata=metadata)

class Exercise(db.Model):
  __tablename__ = 'exercises'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  category = db.Column(db.String)
  equipment_needed = db.Column(db.Boolean)
  # In the first part put the class name you have a relationship with
  # After back_populates you put the variable name you stated in WorkoutExercises and connected to the respective classes
  workoutexercises = db.relationship('WorkoutExercises', back_populates='exercise', cascade='all, delete-orphan')

class Workout(db.Model):
  __tablename__ = 'workouts'
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  duration_minutes = db.Column(db.Integer)
  notes = db.Column(db.String)
  workoutexercises = db.relationship('WorkoutExercises', back_populates='workout', cascade='all, delete-orphan')

class WorkoutExercises(db.Model):
  __tablename__ = 'workoutexercises'
  id = db.Column(db.Integer, primary_key=True)
  workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
  exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'))
  reps = db.Column(db.Integer)
  sets = db.Column(db.Integer)
  duration_seconds = db.Column(db.Integer)
  workout = db.relationship('Workout', back_populates='workoutexercises')
  exercise = db.relationship('Exercise', back_populates='workoutexercises')