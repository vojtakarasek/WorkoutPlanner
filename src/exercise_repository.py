from enum import Enum


class BodyPart(Enum, str):
    abdominals = 'břicho'
    back = 'záda'
    arms = 'ruce'
    chest = 'prsa'
    shoulders = 'ramena'
    quads = 'stehna'
    calves = 'lýtka'


class Level(Enum, str):
    beginner = 'začátečník'
    intermediate = 'středně pokročilý'
    advanced = 'pokročilý'
    pro = 'profík'


class ExerciseRepository:
    def load(self, file_name):
        pass

    def get_all(self) -> list:
        pass

    def get_for_body_part(self, body_part) -> list:
        pass
