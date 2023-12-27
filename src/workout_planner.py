from exercise_repository import ExerciseRepository
from workout import Workout
from user_requirements import UserRequirements


class WorkoutPlanner:
    def __init__(self, repository: ExerciseRepository):
        self.repository = repository

    def create_plan(self, user_req: UserRequirements): #-> Workout:  # returns class Workout
        #body_parts_given = user_req.body_part_reqs()
        return self.repository.get_for_body_part(user_req)
