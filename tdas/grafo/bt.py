from ejemplos import ejemplo_bt, reinas
import time

DIMENSION = 8
FUERZA_BRUTA = True


def es_compatible(grafo, puestos):
    for v in puestos:
        for w in puestos:
            if v == w:
                continue
            if w in grafo.adyacentes(v):
                return False
    return True


def _ubicacion_FB(grafo, vertices, v_actual, puestos, n):
    if v_actual == len(grafo):
        return False
    if len(puestos) == n:
        return es_compatible(grafo, puestos)
    # Mis opciones son poner acá, o no
    puestos.add(vertices[v_actual])
    if _ubicacion_FB(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_FB(grafo, vertices, v_actual + 1, puestos, n)


def _ubicacion_BT(grafo, vertices, v_actual, puestos, n):
    if v_actual == len(grafo):
        return False
    if len(puestos) == n:
        return es_compatible(grafo, puestos)

    if not es_compatible(grafo, puestos):
        return False

    # Mis opciones son poner acá, o no
    puestos.add(vertices[v_actual])
    if _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n):
        return True
    puestos.remove(vertices[v_actual])
    return _ubicacion_BT(grafo, vertices, v_actual + 1, puestos, n)


def ubicacion(grafo, n):
    puestos = set()
    vertices = grafo.keys()
    if FUERZA_BRUTA:
        _ubicacion_FB(grafo, vertices, 0, puestos, n)
    else:
        _ubicacion_BT(grafo, vertices, 0, puestos, n)
    return puestos


def _ubicacion_BT_todos(grafo, vertices, v_actual, puestos, n):
    if v_actual == len(grafo) and len(puestos) != n:
        return []
    if len(puestos) == n:
        return [set(puestos)] if es_compatible(grafo, puestos) else []

    if not es_compatible(grafo, puestos):
        return []

    # Mis opciones son poner acá, o no
    puestos.add(vertices[v_actual])
    soluciones_con = _ubicacion_BT_todos(grafo, vertices, v_actual + 1, puestos, n)
    puestos.remove(vertices[v_actual])
    soluciones_sin = _ubicacion_BT_todos(grafo, vertices, v_actual + 1, puestos, n)
    return soluciones_con + soluciones_sin


def ubicacion_todos(grafo, n):
    return _ubicacion_BT_todos(grafo, grafo.keys(), 0, set(), n)


if __name__ == "__main__":
    inicio = time.time()
    print(ubicacion(reinas(DIMENSION), DIMENSION))  # https://drive.google.com/file/d/1_j6XaxVGBtJiEmtORGmZimuOvvwJG5ad/view?usp=sharing
    fin = time.time()
    print(int((fin - inicio) * 1000), "mili sec")