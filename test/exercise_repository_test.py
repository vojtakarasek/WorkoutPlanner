from src.exercise_repository import ExerciseRepository


def test_1():
    repository = ExerciseRepository()
    repository.load("json1.json")
    assert repository.get_all() == 1


def test_2():
    assert 2 == 2


