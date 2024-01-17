from src.body_part_enum import BodyPart


def test_body_part_enum_values():
    assert BodyPart.arms == 'paže'
    assert BodyPart.shoulders == 'ramena'
    assert BodyPart.back == 'záda'
    assert BodyPart.abdominals == 'břicho'
    assert BodyPart.chest == 'prsa'
    assert BodyPart.quads == 'stehna'
    assert BodyPart.calves == 'lýtka'


def test_body_part_enum_comparasion():
    BodyPart.quads == BodyPart.quads
    BodyPart.arms != BodyPart.calves
