def calculer_coordonnees_clou(a, b, c, d, e):
    tuple_t0 = [(b * -1) / 2, c / 2]
    tuple_t1 = [(b * -1) / 2, (-1 * c) / 2]
    tuple_t2 = [((b * -1) / 2) - d, -1 * a / 2]
    tuple_t3 = [((b * -1) / 2) - d, a / 2]
    tuple_k0 = [b / 2 + e, 0]
    tuple_k1 = [b / 2, -1 * c / 2]
    tuple_k2 = [b / 2, c / 2]
    return [('pt_0', tuple_t0), ('pt_01', tuple_t1), ('pt_2', tuple_t2), ('pt_3', tuple_t3), ('pk_2', tuple_k2), ('pk_0', tuple_k0), ('pk_1', tuple_k1)]
