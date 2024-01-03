from exercise import Exercise
import json
import random


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

    def get_for_body_part(self, body_part_given, level) -> list[Exercise]:
        self.exercises_body_part = []
        for exercise in self.exercises:
            controller = 0
            #if len(self.exercises_body_part) == 8:
                #break
            #else:
            if len(body_part_given) == 1:
                if body_part_given[0] in exercise.body_part:
                    self.exercises_body_part.append(exercise)

            else:
                for i in body_part_given:
                    if controller == 0:
                            #if len(self.exercises_body_part) == 8:
                                #break
                            #else:
                            if i in exercise.body_part:
                                self.exercises_body_part.append(exercise)
                                controller += 1

        self.get_for_level(level)

        return self.exercises_level

    def get_for_level(self, level_given):
        self.exercises_level = []

        for exercise in self.exercises_body_part:
            if level_given in exercise.level:
                self.exercises_level.append(exercise)
                self.exercises_body_part.remove(exercise)

        if len(self.exercises_level) < 8:
            self.give_random(self.exercises_body_part, 8 - len(self.exercises_level), len(self.exercises_body_part), False)

        elif len(self.exercises_level) == 8:
            self.exercises_body_part = self.exercises_level

        else:
            self.give_random(self.exercises_level, 8, len(self.exercises_level), True)

    def give_random(self, exercises, exercises_needed, length, delete: bool):
        used_numbers = []
        if delete:
            self.exercises_level = []
            for _ in range(exercises_needed):
                random_int = random.randint(0, length)
                self.exercises_level.append(exercises[random_int])
                used_numbers.append(random_int)

        else:
            for _ in range(exercises_needed):
                random_int = random.randint(0, length - 1)
                self.exercises_level.append(exercises[random_int])

