from exercise import Exercise
from user_requirements import UserRequirements


class WorkoutPlanner:

    def __init__(self, data1: Exercise, data2: UserRequirements):
        self.data1 = data1
        self.data2 = data2

    def create_plan(self) -> list:
        pass
