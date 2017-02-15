class MinStack(object):

    def __init__(self):
        # do some intialize if necessary
        self.stack = []
    def push(self, number):
        # write yout code here
        self.stack.append(number)
    def pop(self):
        # pop and return the top item in stack
        return self.stack.pop()
    def min(self):
        # return the minimum number in stack
        min = self.stack[0]
        for i in range(1,len(self.stack)):
            if min > self.stack[i]:
                min = self.stack[i]
        return min