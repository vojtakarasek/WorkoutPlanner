from exercise import Exercise
import json


class ExerciseRepository:
    def __init__(self):
        self.json_data = None

    def load(self, file_name):
        with open(file_name) as v:
            self.json_data = json.load(v)
            v.close()
            return self.json_data

    def get_all(self) -> list[Exercise]:
        pass

    def get_for_body_part(self, body_part) -> list[Exercise]:
        pass
