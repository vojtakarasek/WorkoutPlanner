from enum import Enum


class ExerciseRepository(Enum):
    def load(self, file_name):
        pass

    def get_all(self) -> list:
        pass

    @classmethod
    def get_for_body_part(cls, body_part) -> list:
        pass
