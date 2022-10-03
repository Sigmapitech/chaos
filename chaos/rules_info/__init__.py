ruleset = [
    f'{x}{id_y}'
    for x, y in (
        ('A', 4), ('C', 3), ('F', 9), ('G', 9),
        ('H', 3), ('L', 6), ('O', 4), ('V', 3)
    )
    for id_y in range(1, y + 1)
]

__all__ = ('ruleset',)
