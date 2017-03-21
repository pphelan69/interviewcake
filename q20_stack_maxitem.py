class Stack:

    # initialize an empty list for stack items and also for max integer items
    def __init__(self):
        self.items = []
        self.max   = []


    # push a new item onto item list and update max list if needed
    def push(self, item):
        self.items.append(item)
        if len(self.max) == 0 or item >= self.max[-1]:
            self.max.append(item)


    # remove the last item from items list and check to see if this value is a max and if so remove from max list.
    def pop(self):
        if len(self.items) == 0:
            return None
        if self.items[-1] == self.max[-1]:
            self.max.pop()

        return self.items.pop()


    # see what the last item is
    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]


    def getMax(self):
        if len(self.max) == 0:
            return None
        else:
            return self.max[-1]





x = Stack()
x.push(10)
x.push(8)
x.push(9)
x.push(3)
x.push(2)
x.push(11)
x.pop()
print(x.getMax())

