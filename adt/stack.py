class Stack:

    def __init__(self):
        self.__stack = []
        self.__top = -1
        self.__max_size = 10

    def get(self):
        return self.__stack

    def push(self, val):
        self.__stack.append(val)
        self.__top += 1

    def pop(self):
        if self.is_empty():
            return None

        val = self.__stack[self.__top]
        self.__top -= 1
        self.__stack = self.__stack[:self.__top + 1]
        return val

    def is_empty(self):
        return self.__top == -1

    def is_full(self):
        return self.__top == self.__max_size - 1


stack = Stack()
print(stack.get())
stack.push(1)
print(stack.get())
print(stack.pop())
print(stack.pop())
print(stack.get())
