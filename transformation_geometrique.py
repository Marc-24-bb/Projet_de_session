def calculer_reflexion_point(tuple, axe):
    reflexion_point_x = None
    reflexion_point_y = None
    if axe == 'x':
        reflexion_point_y = tuple[1] * -1
        reflexion_point_x = tuple[0]
    elif axe =='y':
        reflexion_point_x = tuple[0] * -1
        reflexion_point_y = tuple[1]
    return reflexion_point_x, reflexion_point_y