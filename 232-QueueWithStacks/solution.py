# This is NOT a good solution. It is just a solution that works.
# Need to Redo this problem with a better solution.
# Doesnt even use 2 stacks. Just uses a list.

# 37ms (42.50%), 16.63MB (20.07%)

class MyQueue:

    def __init__(self):
        self.ftb = []
    
    def push(self, x: int) -> None:
        self.ftb.append(x)

    def pop(self) -> int:
        return self.ftb.pop(0)
        
    def peek(self) -> int:
        return self.ftb[0]

    def empty(self) -> bool:
        if len(self.ftb) >0:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()