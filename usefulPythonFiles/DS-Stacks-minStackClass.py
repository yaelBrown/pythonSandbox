# Create Stack => stack = myStack(5); where 5 is size of stack
# Create Queue => queue = myQueue(5); where 5 is size of queue
# Stack Functions => isEmpty(), isFull(), top()
# Queue Functions => enqueue(int),dequeue(),isEmpty(),getSize()

from Stack import MyStack

class MinStack:
    # Constructor
    def __init__(self):
        # Write your code here
        self._stack = []
        self._len = 0
        self._minVal = 0
        

    def pop(self):
        # Write your code here
        if self._len == 0:
            return None
        else:
            out = self._stack[-1]
            self._stack.remove(out)
            self._len -= 1
            return out

    # Pushes value into new stack
    def push(self, value):
        # Write your code here
        self._stack.append(value)
        self._len += 1
        if value < self._minVal:
            self._minVal = value


    # Returns minimum value from new stack in constant time
    def min(self):
        # Write your code here
        return self._minVal

    # Write any helper functions here




from Stack import MyStack

class MinStack:
    # Constructor
    def __init__(self):
        self.min_stack = MyStack()
        self.main_stack = MyStack()

    # Removes and returns value from min_stack
    def pop(self):
        self.min_stack.pop()
        return self.main_stack.pop()

    # Pushes values into min_stack
    def push(self, value):
        self.main_stack.push(value)
        if self.min_stack.is_empty() or self.min_stack.peek() > value :
            self.min_stack.push(value)
        else:
            self.min_stack.push(self.min_stack.peek())
            
    # Returns minimum value from newStack in O(1) Time
    def min(self):
        if not self.min_stack.is_empty():
            return self.min_stack.peek()
        # In case the stack is empty
        return None
        
if __name__ == "__main__" :
    stack = MinStack()
    stack.push(5)
    stack.push(0)
    stack.push(2)
    stack.push(4)
    stack.push(1)
    stack.push(3)
    stack.push(0)
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    stack.push(-2)
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
    stack.pop()
    print("Main stack:", stack.main_stack.stack_list)
    print("Min stack:", stack.min_stack.stack_list)
    print("Minimum value: " + str(stack.min()))
