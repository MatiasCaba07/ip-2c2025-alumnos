# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

elementos = []
norte = 0
i = 0
j = 0

def inicialización(vals):
    global elementos, norte, i, j
    elementos = list(vals)
    norte = len(elementos)
    i = 0
    j = 0

def paso():
    global elementos, norte, i, j

    # Si ya terminamos
    if i >= norte - 1:
        return {"done": True}

    # Si j llegó al final de la pasada, avanzamos i
    if j >= norte - 1 - i:
        i += 1
        j = 0

        if i >= norte - 1:
            return {"done": True}

    # Índices a comparar
    a = j
    b = j + 1
    swap = False

    # Comparación + swap si corresponde
    if elementos[a] > elementos[b]:
        elementos[a], elementos[b] = elementos[b], elementos[a]
        swap = True

    # Avanzar para el próximo paso
    j += 1

    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False
    }
