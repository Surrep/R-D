from memory.node import Node


class Trie():

    def __init__(self, root):
        self.root = root
        self.branch = root

    def absorb(self, stream):
        for sample in stream:
            self.branch = self.branch.follow(sample)

        self.branch = self.root
        return self
