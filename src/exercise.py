from dataclasses import dataclass


@dataclass
class Exercise:
    name: str
    description: str
    body_part: str
    level: str
    repetitions: int
    series: int

