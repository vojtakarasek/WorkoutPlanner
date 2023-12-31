from gui import GUI
from src.exercise_repository import ExerciseRepository
from src.workout_planner import WorkoutPlanner


def main():
    repository = ExerciseRepository()
    repository.load('../data/exercises.json')
    planner = WorkoutPlanner(repository)
    app = GUI()
    app.use_planner(planner)
    app.mainloop()


if __name__ == "__main__":
    main()
