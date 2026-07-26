#!/usr/bin/env python3

from app import app
from models import *

with app.app_context():
  # Delete all data to preventing duplicates
  WorkoutExercises.query.delete()
  Workout.query.delete()
  Exercise.query.delete()
