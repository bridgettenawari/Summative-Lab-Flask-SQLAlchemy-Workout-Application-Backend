from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Exercise(db.Model):
  __tablename__ = 'exercises'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  category = db.Column(db.String, nullable=False)
  equipment_needed = db.Column(db.Boolean, default=False)
  # In the first part put the class name you have a relationship with
  # After back_populates you put the variable name you stated in WorkoutExercises and connected to the respective classes
  workoutexercises = db.relationship('WorkoutExercises', back_populates='exercise', cascade='all, delete-orphan')

  # Model Validation
  @validates('name') # Pass the key mentioned in the function into the brackets
  def validate_name(self, key, value):
    if value is not None and 50 > len(value) > 3:
      raise ValueError("Name must be longer than 3 characters and less than 50 characters.")
    return value

  @validates('category')
  def validate_category(self, key, value):
    if value is not None and 20 > len(value) > 3:
      raise ValueError("Category must be longer than 3 characters and less than 20 characters.")
    return value

class Workout(db.Model):
  __tablename__ = 'workouts'
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date)
  duration_minutes = db.Column(db.Integer, nullable=False)
  notes = db.Column(db.String(500))
  workoutexercises = db.relationship('WorkoutExercises', back_populates='workout', cascade='all, delete-orphan')

  # Table constraints
  __table_args__ = (
    db.CheckConstraint('duration_minutes >= 0')
  )

  # Model Validation
  @validates('notes')
  def validate_notes(self, key, value):
    if value is not None and  500 > len(value) > 0:
      raise ValueError("Duration cannot be less than 0 minutes.")
    return value

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

  # Table constraints
  __table_args__ = (
    db.CheckConstraint('sets >= 0'),
    db.CheckConstraint('duration_seconds >= 0'),
    db.CheckConstraint('reps >= 0')
  )