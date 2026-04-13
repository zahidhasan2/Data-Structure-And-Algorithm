
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack)!=0:
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if len(self.stack)!=0:
            return self.stack[-1]
        return "Stack is empty"
    
    def is_empty(self):
        return len(self.stack)==0

    def display(self):
        print("stack is: ",self.stack)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.is_empty()
print("Top element:", s.peek())
print("Pop:", s.pop())
s.display()
