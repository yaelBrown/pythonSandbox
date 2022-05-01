from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    if queue.size() < k:
        return -1
    tempQ = MyQueue()
    cnt = 0

    while cnt != k:
        tempQ.enqueue(queue.dequeue())
        cnt += 1

    tempQ.rear().insert_tail(queue.dequeue())

    return tempQ


# 1.Push first k elements in queue in a stack.
# 2.Pop Stack elements and enqueue them at the end of queue
# 3.Dequeue queue elements till "k" and append them at the end of queue

def reverseK(queue, k):
    # Handling invalid input
    if queue.is_empty() is True or k > queue.size() or k < 0:
        return None
    # Creating stack for reversing the elements
    stack = MyStack()
    for i in range(k):
        stack.push(queue.dequeue())
    while stack.is_empty() is False:
        queue.enqueue(stack.pop())
    size = queue.size()
    for i in range(size - k):
        queue.enqueue(queue.dequeue())
    return queue