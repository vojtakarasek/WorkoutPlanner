from dataclasses import dataclass
from level_enum import Level
from body_part_enum import BodyPart


@dataclass
class Exercise:
    name: str
    description: str
    body_part: BodyPart
    level: Level
    repetitions: int
    series: int

