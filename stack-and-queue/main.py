from queue import Queue
from stack import Stack
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print('value from peek -->',queue.peek())
    print(queue.dequeue())
    # print(queue.dequeue()) uncomment this line to see the exception
    print(queue.is_empty())



    print("=====================================")



    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print('value from peek -->',stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    # print(stack.pop()) uncomment this line to see the exception
    
    print('is it empty stack -->',stack.is_empty())
    





    


