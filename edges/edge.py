
class EdgeBox():

    def __init__(self):
        self.leftmost_col = None
        self.rightmost_col = None
        self.topmost_row = None
        self.bottommost_row = None

        self.orientation = None
        self.spots = []

    def absorb(self, r, c):
        self.spots.append((r, c))

        if(self.topmost_row == None or r < self.topmost_row):
            self.topmost_row = r

        if(self.leftmost_col == None or c < self.leftmost_col):
            self.leftmost_col = c

        if(self.bottommost_row == None or r > self.bottommost_row):
            self.bottommost_row = r

        if(self.rightmost_col == None or c > self.rightmost_col):
            self.rightmost_col = c

    def area(self):
        return (self.bottommost_row - self.topmost_row) * (self.rightmost_col - self.leftmost_col)

    def index_tuple(self):
        return (slice(self.topmost_row, self.bottommost_row),
                slice(self.leftmost_col, self.rightmost_col))
