from transformation_geometrique import calculer_reflexion_point, calculer_rotate_point, calculer_inclinaison_point
def test_calculer_reflexion_point():
    calculer_reflexion_point(tuple, axe)
print(calculer_reflexion_point((2,4),'y'))

def test_calculer_rotate_point():
    calculer_rotate_point(tuple_p, tuple_c, angle)
print(calculer_rotate_point((2,4), (0,0), 30))


def test_calculer_inclinaison_point():
    calculer_inclinaison_point(tuple, angle, directon)
print(calculer_inclinaison_point((2,4), (5), 'y'))