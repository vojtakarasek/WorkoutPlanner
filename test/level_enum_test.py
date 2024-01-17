from src.level_enum import Level


def test_level_enum_values():
    assert Level.beginner == 'začátečník'
    assert Level.intermediate == 'středně pokročilý'
    assert Level.advanced == 'pokročilý'


def test_level_enum_comparasion():
    assert Level.beginner == Level.beginner
    assert Level.intermediate != Level.advanced
