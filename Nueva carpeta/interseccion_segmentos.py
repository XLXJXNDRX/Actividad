def orientacion(p, q, r):
    val = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
    if round(val, 9) == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def en_segmento(p, q, r):
    return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

def interseccion(a, b, c, d):
    o1 = orientacion(a, b, c)
    o2 = orientacion(a, b, d)
    o3 = orientacion(c, d, a)
    o4 = orientacion(c, d, b)

    if o1 != o2 and o3 != o4:
        return True

    # Casos colineales
    if o1 == 0 and en_segmento(a, c, b):
        return True
    if o2 == 0 and en_segmento(a, d, b):
        return True
    if o3 == 0 and en_segmento(c, a, d):
        return True
    if o4 == 0 and en_segmento(c, b, d):
        return True

    return False

# Pruebas del punto 2
print("Caso 1:", interseccion((1, 1), (5, 4), (1, 4), (5, 1)))
print("Caso 2:", interseccion((1, 3), (6, 3), (4, 3), (8, 3)))
print("Caso 3:", interseccion((1, 1), (3, 3), (4, 1), (7, 2)))