from transformation_geometrique import calculer_reflexion_point, calculer_rotate_point, calculer_inclinaison_point
def test_calculer_reflexion_point_1():
    assert calculer_reflexion_point((2,4),'x') == (2, -4), 'Erreur'

def test_calculer_reflexion_point_2():
    assert calculer_reflexion_point((2,4),'y') == (-2, 4), 'Erreur'
def test_calculer_rotate_point():
    assert calculer_rotate_point((2,4), 30) == (-0.27,4.46), 'Erreur'


def test_calculer_inclinaison_point_1():
    assert calculer_inclinaison_point((2,4), 5, 'x') == (2.35, 4.0), 'Erreur'
def test_calculer_inclinaison_point_2():
    assert calculer_inclinaison_point((2,4), 5, 'y') == (2.0, 4.17), 'Erreur'

