from src.exercise_repository import ExerciseRepository
import os


def test_videos():
    repository = ExerciseRepository()
    repository.load("test_data/exercises1_test.json")
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
                entry_path = entry.path.replace('../', '')
                if entry_path in videos:
                    pass
                else:
                    a += 1
                    errors.append(entry.path)
    assert a == 0
