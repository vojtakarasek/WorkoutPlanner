from dataclasses import dataclass

from body_part_enum import BodyPart
from level_enum import Level


@dataclass
class UserRequirements:
    body_part: BodyPart
    level: Level
