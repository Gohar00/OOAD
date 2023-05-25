from abc import ABC, abstractmethod
from datetime import datetime

class Exercise(ABC):
    def __init__(self, name, muscle_group):
        self.name = name
        self.muscle_group = muscle_group

    @abstractmethod
    def __str__(self):
        pass

class CardioExercise(Exercise):
    def __init__(self, name, muscle_group, distance):
        super().__init__(name, muscle_group)
        self.distance = distance

    def __str__(self):
        return f"{self.name} (cardio exercise, targets {self.muscle_group}, {self.distance} km)"

class StrengthExercise(Exercise):
    def __init__(self, name, muscle_group, sets, reps, weight):
        super().__init__(name, muscle_group)
        self.sets = sets
        self.reps = reps
        self.weight = weight

    def __str__(self):
        return f"{self.name} (strength exercise, targets {self.muscle_group}, {self.sets} sets of {self.reps} reps at {self.weight} kg)"

class User:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.fav_exercises = []

    def add_favorite_exercise(self, exercise):
        self.fav_exercises.append(exercise)

    def __str__(self):
        return f"{self.name} ({self.contact_info}), favorites: {', '.join(str(e) for e in self.fav_exercises)}"

class WorkoutPlan:
    def __init__(self, user, exercises, duration_days):
        self.user = user
        self.exercises = exercises
        self.duration_days = duration_days

    def __str__(self):
        return f"{self.user.name}'s workout plan ({self.duration_days} days): {', '.join(str(e) for e in self.exercises)}"

class FitnessTracker:
    def __init__(self):
        self.users = []
        self.workout_plans = []
        self.completed_workouts = []

    def add_user(self, user):
        self.users.append(user)

    def create_workout_plan(self, user, exercises, duration_days):
        plan = WorkoutPlan(user, exercises, duration_days)
        self.workout_plans.append(plan)
        return plan

    def complete_workout(self, user, workout_plan):
        workout_date = datetime.now().date()
        completed_workout = (user, workout_plan, workout_date)
        self.completed_workouts.append(completed_workout)

    def __str__(self):
        return f"Fitness tracker: {len(self.users)} users, {len(self.workout_plans)} workout plans, {len(self.completed_workouts)} completed workouts"

# Import the FitnessTrackingSystem class
from fitness_tracking_system import FitnessTrackingSystem

# Create a new instance of the FitnessTrackingSystem
fts = FitnessTrackingSystem()

# Create some exercises
fts.create_exercise("Push-ups", "Chest")
fts.create_exercise("Squats", "Legs")
fts.create_exercise("Running", "Cardio")

# Create some users
fts.create_user("Alice", "alice@example.com")
fts.create_user("Bob", "bob@example.com")

# Add favorite exercises for users
fts.add_favorite_exercise("Alice", "Push-ups")
fts.add_favorite_exercise("Bob", "Running")
fts.add_favorite_exercise("Bob", "Squats")

# Create workout plans
fts.create_workout_plan("Alice", ["Push-ups", "Squats"], 30)
fts.create_workout_plan("Bob", ["Running", "Squats"], 45)

# Log workout progress
fts.log_workout_progress("Alice", "Push-ups", 10, "2023-04-01")
fts.log_workout_progress("Alice", "Squats", 20, "2023-04-02")
fts.log_workout_progress("Bob", "Running", 3.5, "2023-04-02")
fts.log_workout_progress("Bob", "Squats", 15, "2023-04-02")

# Print user workout history
print(fts.get_user_workout_history("Alice"))
print(fts.get_user_workout_history("Bob"))

# Print recommended exercises for users
print(fts.get_recommended_exercises("Alice"))
print(fts.get_recommended_exercises("Bob"))

# Print most popular exercises
print(fts.get_most_popular_exercises())
