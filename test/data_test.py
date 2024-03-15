from src.exercise_repository import ExerciseRepository
import os


def test_videos():
    repository = ExerciseRepository()
    repository.load("../data/exercises1.json")
    repository.get_all()
    exercises = repository.exercises
    videos = []
    a = 0
    errors = []

    for i in exercises:
        videos.append(i.video)

    basepath = '../data/cviky/'
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_file():
                if entry.path in videos:
                    pass
                else:
                    a += 1
                    errors.append(entry.path)
    assert a == 0
