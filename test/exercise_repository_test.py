from src.exercise_repository import ExerciseRepository


def test_load():
    repository = ExerciseRepository()
    repository.load("test/json1.json")
    assert len(repository.get_all()) == 1


def test_2():
    assert 2 == 2


