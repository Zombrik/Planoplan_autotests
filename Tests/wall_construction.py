from Utils import *


def test_wall_constr_by_edge():
    assert wall_construction_by_edge() == 'good'


def test_wall_constr_by_center():
    assert wall_construction_by_center() == 'good'


def test_wall_constr_by_room():
    assert wall_construction_by_room() == 'good'


