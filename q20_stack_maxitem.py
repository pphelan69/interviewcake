class Stack:
    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]


class MaxStack:

    def __init__(self):
        self.items = Stack()
        self.max   = Stack()


    def push(self,item):
        self.items.push(item)

        if self.max.peek() is None or item >= self.max.peek():
            self.max.push(item)


    def pop(self):
        item = self.items.pop()

        if item == self.max.peek():
            self.max.pop()

        return item


    def getMax(self):
        return self.max.peek()




x = MaxStack()
x.push(10)
x.push(8)
x.push(9)
x.push(3)
x.push(2)
x.push(11)
x.pop()
print(x.getMax())

