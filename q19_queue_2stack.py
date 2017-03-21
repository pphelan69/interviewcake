class Queue:

    def __init__(self):
        self.in_stack  = []
        self.out_stack = []



    def enqueue(self,item):
        self.in_stack.append(item)


    def dequeue(self):

        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())

            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()


    def printStacks(self):
        print(self.in_stack)
        print(self.out_stack)





x = Queue()
x.enqueue('a')
x.enqueue('b')
x.enqueue('c')    
x.dequeue()
x.enqueue('d')
x.enqueue('e')
x.dequeue()

x.printStacks()

