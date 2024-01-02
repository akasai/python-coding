class Queue:
    def __init__(self):
        self.__max_size = 4
        self.__q = [None] * self.__max_size
        self.__rear = self.__front = -1

    def is_full(self):
        return (self.__rear + 1) % self.__max_size == self.__front

    def is_empty(self):
        return self.__rear == self.__front == -1

    def push(self, value):
        if self.is_full():
            return

        if self.is_empty():
            self.__rear = self.__front = 0
        else:
            self.__rear = (self.__rear + 1) % self.__max_size

        self.__q[self.__rear] = value

        return

    def pop(self):
        if self.is_empty():
            return None

        item = self.__q[self.__front]

        if self.__front == self.__rear:
            self.__rear = self.__front = -1
        else:
            self.__front = (self.__front + 1) % self.__max_size

        return item


q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
print(q.pop())
print(q.pop())
