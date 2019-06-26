
class Resource:
    def __init__(self, attrs, stub='%s%s.%s'):
        self.stub = stub
        self.attrs = attrs
        self.string = self.stub % self.attrs
