# Frontier structure for BFS
class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class PriorityQueueFrontier(QueueFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            index = 0
            minVal = self.frontier[0].hamming() + self.frontier[0].manhattan()
            for i in range(1, len(self.frontier)):
                temp = self.frontier[i].hamming() + self.frontier[i].manhattan()
                if temp <= minVal:
                    minVal = temp
                    index = i
            node = self.frontier[index]
            self.frontier.remove(self.frontier[index])
            return node


class PriorityQueueHammingFrontier(QueueFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            index = 0
            minHamming = self.frontier[0].hamming()
            for i in range(1, len(self.frontier)):
                temp = self.frontier[i].hamming()
                if temp <= minHamming:
                    minHamming = temp
                    index = i
            node = self.frontier[index]
            self.frontier.remove(self.frontier[index])
            return node


class PriorityQueueManhattanFrontier(QueueFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            index = 0
            minManhattan = self.frontier[0].manhattan()
            for i in range(1, len(self.frontier)):
                temp = self.frontier[i].manhattan()
                if temp <= minManhattan:
                    minManhattan = temp
                    index = i
            node = self.frontier[index]
            self.frontier.remove(self.frontier[index])
            return node


class PriorityQueueAStarFrontier(QueueFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            index = 0
            minVal = self.frontier[0].moves + self.frontier[0].manhattan()
            for i in range(1, len(self.frontier)):
                temp = self.frontier[i].moves + self.frontier[i].manhattan()
                if temp <= minVal:
                    minVal = temp
                    index = i
            node = self.frontier[index]
            self.frontier.remove(self.frontier[index])
            return node
