from exercise import Exercise
import json

from src.body_part_enum import BodyPart
from src.level_enum import Level


class ExerciseRepository:
    def __init__(self):
        self.exercises = []
        self.exercises_body_part = []
        self.exercises_level = []

    def load(self, file_name):
        self.exercises = []
        with open(file_name, encoding='utf-8') as v:
            json_data = json.load(v)
            for exercise in json_data["exercises"]:
                self.exercises.append(
                    Exercise(exercise["name"],
                             exercise["description"],
                             exercise["body_parts"],
                             exercise["level"],
                             exercise["repetitions"],
                             int(exercise["series"]),
                             exercise["video"]
                             )
                )

    def get_all(self) -> list[Exercise]:
        return self.exercises

    def get_for_body_part(self, body_part_given: [BodyPart]) -> list[Exercise]:
        exercises_body_part = []
        for exercise in self.exercises:
            controller = 0
            if len(body_part_given) == 1:
                if body_part_given[0] in exercise.body_part:
                    exercises_body_part.append(exercise)

            else:
                for i in body_part_given:
                    if controller == 0:
                        if i in exercise.body_part:
                            exercises_body_part.append(exercise)
                            controller += 1

        return exercises_body_part



