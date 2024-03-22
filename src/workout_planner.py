import random

from exercise_repository import ExerciseRepository
from src.exercise import Exercise
from src.level_enum import Level
from user_requirements import UserRequirements


class WorkoutPlanner:
    def __init__(self, repository: ExerciseRepository):
        self.repository = repository

    def create_plan(self, req: UserRequirements, count: int):
        all_available = self.repository.get_for_body_part(req.body_part)
        return self.get_for_level(all_available, req.level, count)

    def get_for_level(self, exercises_body_part: [Exercise], level_given: Level, count: int):
        exercises_level = []

        for exercise in exercises_body_part:
            if level_given in exercise.level:
                exercises_level.append(exercise)

        exercises_body_part = [item for item in exercises_body_part if item not in exercises_level]

        if len(exercises_level) < count:
            return self.add_random(exercises_level, count - len(exercises_level), exercises_body_part)

        elif len(exercises_level) > count:
            return self.remove_random(exercises_level, len(exercises_level) - count)

        return exercises_level

    @staticmethod
    def add_random(exercises_level, count, exercises_body_part):
        for _ in range(count):
            random_int = random.randint(0, len(exercises_body_part) - 1)
            exercises_level.append(exercises_body_part[random_int])
            exercises_body_part.pop(random_int)
        return exercises_level

    @staticmethod
    def remove_random(exercises_level, count):
        for _ in range(count):
            random_int = random.randint(0, len(exercises_level) - 1)
            exercises_level.pop(random_int)
        return exercises_level
