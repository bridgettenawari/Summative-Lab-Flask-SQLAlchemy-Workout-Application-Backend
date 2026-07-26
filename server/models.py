from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import date
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
  @validates('name')
  def validate_name(self, key, value):
    if not value or len(value) <= 3 or len(value) >= 50:
        raise ValueError("Name must be longer than 3 characters and less than 50 characters.")
    return value


  @validates('category')
  def validate_category(self, key, value):
    if not value or len(value) <= 3 or len(value) >= 20:
        raise ValueError("Category must be longer than 3 characters and less than 20 characters.")
    return value

  def __repr__(self):
   return f"<Exercise {self.id}, name={self.name}, category={self.category}, equipment_needed={self.equipment_needed}"


class Workout(db.Model):
  __tablename__ = 'workouts'
  id = db.Column(db.Integer, primary_key=True)
  date = db.Column(db.Date, default=date.today)
  duration_minutes = db.Column(db.Integer, nullable=False)
  notes = db.Column(db.String(500))
  workoutexercises = db.relationship('WorkoutExercises', back_populates='workout', cascade='all, delete-orphan')

  # Table constraints
  __table_args__ = (
    db.CheckConstraint('duration_minutes >= 0'),
  )

  # Model Validation
  @validates('notes')
  def validate_notes(self, key, value):
    if not value or len(value.strip()) == 0:
        raise ValueError("Notes cannot be empty.")
    return value
  
  def __repr__(self):
    return f"<Workout {self.id}, date={self.date}, duration_minutes={self.duration_minutes}, notes={self.notes}"

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
    db.CheckConstraint('reps >= 0'),
  )

  def __repr__(self):
    return f"<WorkoutExercise {self.id}, reps={self.reps}, sets={self.sets}, duartion_seconds={self.duration_seconds}"