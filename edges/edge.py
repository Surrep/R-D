
class Edge:

    def __init__(self, r, c, orientation):
        self.start = (r, c)
        self.visited = {self.start}
        self.orientation = orientation
        self.length = 0

    def incorporate(self, r, c, orientation):
        if orientation is self.orientation:
            self.visited.add((r, c))
        else:
            return Edge(r, c, orientation)
