from src.body_part_enum import BodyPart
from src.level_enum import Level
from src.user_requirements import UserRequirements


def test_user_requirements_passes_level():
    user_req = UserRequirements([BodyPart.calves], Level.beginner)
    assert Level.beginner == user_req.level


def test_user_requirements_passes_bodypart():
    user_req = UserRequirements([BodyPart.calves], Level.beginner)
    assert [BodyPart.calves] == user_req.body_part
