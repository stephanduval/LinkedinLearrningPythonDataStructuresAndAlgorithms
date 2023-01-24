"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # return len(self.items) == 0
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# If this is the main file being run (IE its not imported then execute the following code, otherwise execute the class called "Stack")
if __name__ == "__main__":
    s = Stack()   # call the constructor of the stack

    print(s)
    print(s.is_empty())
    s.push(3)
    s.push(5)
    print(s)
    s.push(7)

    print(s)
    print(s.pop())
    print(s)
    print(s.peek())
    print(s.size())
    print(s.is_empty())
