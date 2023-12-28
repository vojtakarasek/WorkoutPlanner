from src.exercise_repository import ExerciseRepository
from src.exercise import Exercise
from src.body_part_enum import BodyPart


def test_load():
    repository = ExerciseRepository()
    repository.load("../data/json1.json")
    assert len(repository.get_all()) == 1


def test_load2():
    repository = ExerciseRepository()
    repository.load("../data/json2.json")
    assert len(repository.get_all()) == 2


def array_equals(a, b) -> bool:
    if len(a) != len(b):
        return False
    for i in range(0, len(a)):
        if a[i] != b[i]:
            return False
    return True


def test_get_all():
    repository = ExerciseRepository()
    repository.load("../data/json1.json")
    expected = [
        Exercise(name="klik", description="ruce u na úrovni ramenou, s nádechem dolů, s výdechem nahoru",
                 body_part=["paže", "prsa"], level="začátečník", repetitions=10, series=3)]
    assert array_equals(repository.get_all(), expected)


def test_get_for_body_part():
    repository = ExerciseRepository()
    repository.load("../data/json1.json")
    assert len(repository.get_for_body_part([BodyPart.arms])) == 1


def test_get_for_body_part2():
    repository = ExerciseRepository()
    repository.load("../data/json1.json")
    assert len(repository.get_for_body_part([BodyPart.arms, BodyPart.chest])) == 1


def test_get_for_body_part3():
    repository = ExerciseRepository()
    repository.load("../data/json2.json")
    assert len(repository.get_for_body_part([BodyPart('paže'), BodyPart.chest])) == 1


def test_get_for_body_part4():
    repository = ExerciseRepository()
    repository.load("../data/json2.json")
    assert len(repository.get_for_body_part([BodyPart('paže'), BodyPart.quads])) == 2


def test_get_for_body_part_getting_8_exercises():
    repository = ExerciseRepository()
    repository.load("../data/exercises.json")
    assert len(repository.get_for_body_part([BodyPart.arms, BodyPart.quads, BodyPart.quads])) == 8


def test_get_for_body_part_getting_8_exercises_2():
    repository = ExerciseRepository()
    repository.load("../data/exercises.json")
    assert len(repository.get_for_body_part([BodyPart.calves])) == 8


def test_get_for_body_part_getting_8_exercises_3():
    repository = ExerciseRepository()
    repository.load("../data/exercises.json")
    assert len(repository.get_for_body_part([BodyPart.calves, BodyPart.calves])) == 8


def test_get_for_body_part_getting_8_exercises_4():
    repository = ExerciseRepository()
    repository.load("../data/exercises.json")
    assert len(repository.get_for_body_part([BodyPart.back, BodyPart.chest])) == 8


def test_get_for_body_part_no_similar_exercises():
    repository = ExerciseRepository()
    repository.load("../data/json1.json")
    assert len(repository.get_for_body_part([BodyPart('paže'), BodyPart.chest])) == 1
