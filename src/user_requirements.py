from dataclasses import dataclass

from src.body_part_enum import BodyPart
from src.level_enum import Level


@dataclass
class UserRequirements:
    body_part: BodyPart
    level: Level
