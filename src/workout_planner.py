from exercise_repository import ExerciseRepository
from user_requirements import UserRequirements


class WorkoutPlanner:
    def __init__(self, repository: ExerciseRepository):
        self.repository = repository

    def create_plan(self, bp_req: UserRequirements, lvl_req: UserRequirements):
        return self.repository.get_for_body_part(bp_req, lvl_req)
