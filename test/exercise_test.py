from src.body_part_enum import BodyPart
from src.level_enum import Level
from src.exercise import Exercise


def test_exercise_name():
    exercise = Exercise(name='klik', description='ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru',
                        body_part=['paže', 'prsa'], level='začátečník', repetitions='10', series=3,
                        video='../data/25.mp4')
    assert exercise.name == 'klik'


def test_exercise_description():
    exercise = Exercise(name='klik', description='ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru',
                        body_part=['paže', 'prsa'], level='začátečník', repetitions='10', series=3,
                        video='../data/25.mp4')
    assert exercise.description == 'ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru'


def test_exercise_body_part():
    exercise = Exercise(name='klik', description='ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru',
                        body_part=['paže', 'prsa'], level='začátečník', repetitions='10', series=3,
                        video='../data/25.mp4')
    assert exercise.body_part == ['paže', 'prsa']


def test_exercise_level():
    exercise = Exercise(name='klik', description='ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru',
                        body_part=['paže', 'prsa'], level='začátečník', repetitions='10', series=3,
                        video='../data/25.mp4')
    assert exercise.level == 'začátečník'


def test_exercise_repetitions():
    exercise = Exercise(name='klik', description='ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru',
                        body_part=['paže', 'prsa'], level='začátečník', repetitions='10', series=3,
                        video='../data/25.mp4')
    assert exercise.repetitions == '10'


def test_exercise_series():
    exercise = Exercise(name='klik', description='ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru',
                        body_part=['paže', 'prsa'], level='začátečník', repetitions='10', series=3,
                        video='../data/25.mp4')
    assert exercise.series == 3


def test_exercise_video():
    exercise = Exercise(name='klik', description='ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru',
                        body_part=['paže', 'prsa'], level='začátečník', repetitions='10', series=3,
                        video='../data/25.mp4')
    assert exercise.video == '../data/25.mp4'


