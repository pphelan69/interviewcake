class Stack:

    # initialize an empty list
    def __init__(self):
        self.items = []


    # push a new item to the last index
    def push(self, item):
        self.items.append(item)


    def pop(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items.pop()


    def peek(self):
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1]


class Queue:

    def __init__(self):
        self.in_stack  = Stack()
        self.out_stack = Stack()


    def enqueue(self,item):
        self.in_stack.push(item)


    def dequeue(self):

        if len(self.out_stack.items) == 0:
            while len(self.in_stack.items) != 0:
                self.out_stack.push(self.in_stack.pop())

            if len(self.out_stack.items) == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()


    def printStacks(self):
        print(self.in_stack.items)
        print(self.out_stack.items)





x = Queue()
x.enqueue('a')
x.enqueue('b')
x.enqueue('c')    
x.dequeue()
x.enqueue('d')
x.enqueue('e')
x.dequeue()

x.printStacks()

