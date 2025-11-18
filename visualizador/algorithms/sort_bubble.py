elementos = []
norte = 0
i = 0
j = 0

def init(vals):
    global elementos, norte, i, j
    elementos = list(vals)
    norte = len(elementos)
    i = 0
    j = 0

def step():
    global elementos, norte, i, j
    if i >= norte - 1:
        return {"done": True}
    if j >= norte - i - 1:
        i += 1
        j = 0
        if i >= norte - 1:
            return {"done": True}
    a = j
    b = j + 1
    swap = False
    if elementos[a] > elementos[b]:
        elementos[a], elementos[b] = elementos[b], elementos[a]
        swap = True
    j += 1

    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False
    }
