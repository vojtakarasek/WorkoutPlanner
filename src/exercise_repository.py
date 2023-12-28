from exercise import Exercise
import json


class ExerciseRepository:
    def __init__(self):
        self.exercises = []

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
                             int(exercise["repetitions"]),
                             int(exercise["series"]))
                )

    def get_all(self) -> list[Exercise]:
        return self.exercises

    def get_for_body_part(self, body_part_given) -> list[Exercise]:
        exercises_body_part = []
        for exercise in self.exercises:
            controller = 0
            if len(exercises_body_part) == 8:
                break
            else:
                if len(body_part_given) == 1:
                    if body_part_given[0] in exercise.body_part:
                        exercises_body_part.append(exercise)

                else:
                    for i in body_part_given:
                        if controller == 0:
                            if len(exercises_body_part) == 8:
                                break
                            else:
                                if i in exercise.body_part:
                                    exercises_body_part.append(exercise)
                                    controller += 1

        return exercises_body_part
