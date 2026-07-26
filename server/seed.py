#!/usr/bin/env python3

from app import app
from models import *
from datetime import date

with app.app_context():
  # Delete all data to preventing duplicates
  WorkoutExercises.query.delete()
  Workout.query.delete()
  Exercise.query.delete()

  exercises_list = [
  Exercise(name="Lift weights", category="Arms", equipment_needed=True),
  Exercise(name="Push ups", category="Core", equipment_needed=False),
  Exercise(name="Squats", category="Glutes", equipment_needed=False),
  Exercise(name="Treadmill",category="Legs", equipment_needed=True), 
  Exercise(name="Morning run", category="Legs"), 
  Exercise(name="Boxing", category="Arms", equipment_needed=True), 
  ]

  workouts_list = [
  Workout(date=date(2026, 7, 11), duration_minutes=20, notes='Wear Gloves'),
  Workout(date=date(2026, 8, 2), duration_minutes=35, notes="Don't bend your knees"),
  Workout(date=date(2026, 7, 20), duration_minutes=30, notes='Wear flat shoes'),
  Workout(duration_minutes=60, notes='Bring headphones'),  # defaults to today
  Workout(date=date(2026, 7, 26), duration_minutes=30, notes="Deep breaths"),
  ]

  db.session.add_all(exercises_list + workouts_list)
  db.session.commit()

  workouts_exercises_list = [
  WorkoutExercises(workout_id=workouts_list[0].id, exercise_id=exercises_list[0].id, reps=10, sets=4, duration_seconds=1200),
  WorkoutExercises(workout_id=workouts_list[0].id, exercise_id=exercises_list[1].id, reps=10, sets=4, duration_seconds=1200),
  WorkoutExercises(workout_id=workouts_list[1].id, exercise_id=exercises_list[2].id, reps=10, sets=6, duration_seconds=2100),
  WorkoutExercises(workout_id=workouts_list[2].id, exercise_id=exercises_list[1].id, reps=10, sets=5, duration_seconds=1800), 
  WorkoutExercises(workout_id=workouts_list[3].id, exercise_id=exercises_list[3].id, reps=10, sets=8, duration_seconds=3600), 
  WorkoutExercises(workout_id=workouts_list[4].id, exercise_id=exercises_list[4].id, reps=10, sets=5, duration_seconds=1800), 
  WorkoutExercises(workout_id=workouts_list[1].id, exercise_id=exercises_list[5].id, reps=10, sets=6, duration_seconds=2100),
  WorkoutExercises(workout_id=workouts_list[2].id, exercise_id=exercises_list[4].id, reps=10, sets=5, duration_seconds=1800),
  WorkoutExercises(workout_id=workouts_list[1].id, exercise_id=exercises_list[0].id, reps=10, sets=6, duration_seconds=2100),
  ]
  db.session.add_all(workouts_exercises_list)
  db.session.commit()