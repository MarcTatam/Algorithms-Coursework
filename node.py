class node:

    neighbours = []
    connections = {}

    def __init__(self, *args, **kwargs):
        return

    def connect(self, target, distance):
        self.neighbours.append(target)
        self.connections[target] = distance
        return

    def connected(self, target)->bool:
        return target in self.neighbours

    def distance(self, target)->int:
        return self.connections[target]
        