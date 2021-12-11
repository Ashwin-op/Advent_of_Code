with open("input.txt") as f:
    plan = {}
    for v, row in enumerate(f.readlines()):
        for h, cell in enumerate(row.strip()):
            plan[(v, h)] = int(cell)


def get_neighbors(point):
    (h, v) = point
    yield (h + 1, v)
    yield (h - 1, v)
    yield (h, v + 1)
    yield (h, v - 1)


def get_lowpoints(plan):
    return [
        (pos, val)
        for pos, val in plan.items()
        if all(plan[n] > val for n in get_neighbors(pos) if n in plan)
    ]


print(sum(val + 1 for _, val in get_lowpoints(plan)))
