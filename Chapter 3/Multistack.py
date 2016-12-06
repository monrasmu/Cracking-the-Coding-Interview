"""
https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter3/31ThreeInOne.py

Made small edits to make it work for all exercises
"""

class MultiStack:

    def __init__(self, stacksize, numstacks):
        self.array = [0] * (stacksize * numstacks)
        self.sizes = [0] * stacksize
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        vals = []
        if self.IsEmpty(stacknum) is not True:
            vals.append(item)

        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item



    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    def Min(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return min(vals)
