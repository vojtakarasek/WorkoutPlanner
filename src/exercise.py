from dataclasses import dataclass
from level_enum import Level
from body_part_enum import BodyPart


@dataclass
class Exercise:
    name: str
    description: str
    body_part: BodyPart
    level: Level
    repetitions: str
    series: int

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description and self.body_part == other.body_part \
            and self.level == other.level and self.repetitions == other.repetitions and self.series == other.series
