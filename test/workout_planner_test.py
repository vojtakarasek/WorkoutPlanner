from src.body_part_enum import BodyPart
from src.exercise_repository import ExerciseRepository
from src.level_enum import Level
from src.user_requirements import UserRequirements
from src.workout_planner import WorkoutPlanner

repo = ExerciseRepository()


def test_add_random_returns_8_exercises():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_all()
    exercises_level = []
    exercises_body_part = []

    for i in range(3):
        exercises_level.append(exercises[i])
        exercises.remove(exercises[i])
    for j in exercises:
        exercises_body_part.append(j)

    assert len(planner.add_random(exercises_level, 8 - len(exercises_level), exercises_body_part)) == 8


def test_add_random_returns_no_duplicates():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_all()
    exercises_body_part = []

    for i in range(8):
        exercises_body_part.append(exercises[i])

    result = planner.add_random([], 8, exercises_body_part)

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            assert result[i] != result[j]


def test_add_random_returns_random_exercises():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_all()
    exercises1 = repo.get_all()

    result1 = planner.add_random([], 8, exercises)
    result2 = planner.add_random([], 8, exercises1)

    assert result1[0] != result2[0] or result1[1] != result2[1] or result1[2] != result2[2] or result1[3] != result2[3]


def test_remove_random_returns_8_exercises():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_all()
    exercises_level = []

    for i in range(14):
        exercises_level.append(exercises[i])

    assert len(planner.remove_random(exercises_level, len(exercises_level) - 8)) == 8


def test_remove_random_returns_no_duplicates():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_all()
    exercises_level = []

    for i in range(8):
        exercises_level.append(exercises[i])

    result = planner.remove_random(exercises_level, len(exercises_level) - 8)

    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            assert result[i] != result[j]


def test_remove_random_returns_random_exercises():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_all()
    exercises_level = []
    exercises_level1 = []

    for i in range(47):
        exercises_level.append(exercises[i])
        exercises_level1.append(exercises[i])

    result1 = planner.remove_random(exercises_level, len(exercises_level) - 8)
    result2 = planner.remove_random(exercises_level1, len(exercises_level1) - 8)

    assert result1[0] != result2[0] or result1[1] != result2[1] or result1[2] != result2[2] or result1[3] != result2[3]


def test_get_for_level_right_level():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_for_body_part(["paže", "záda"])
    result = planner.get_for_level(exercises, Level.intermediate, 8)
    assert result[0].level == "středně pokročilý"


def test_get_for_level_right_body_part():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    exercises = repo.get_for_body_part(["paže"])
    result = planner.get_for_level(exercises, Level.intermediate, 8)
    assert "paže" in result[0].body_part


def test_create_plan():
    planner = WorkoutPlanner(repo)
    repo.load("../test/test_data/exercises.json")
    user_reqs = UserRequirements(["stehna", "paže"], "pokročilý")
    assert len(planner.create_plan(user_reqs, 8)) == 8

