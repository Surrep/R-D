from random import choice


class Node():

    def __init__(self, data):
        self.data = data
        self.children = {None: None}

    def follow(self, sample=None):
        if sample == None:
            sample = choice(list(self.children))
        elif sample not in self.children:
            self.children[sample] = Node(sample)

        return self.children[sample]
