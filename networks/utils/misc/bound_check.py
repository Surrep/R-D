ROW = 0
COL = 1


def in_bounds(shape, r, c):
    return 0 <= r and r < shape[ROW] and 0 <= c and c < shape[COL]
