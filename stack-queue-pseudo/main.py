from pseudo_queue import PseudoQueue

queue = PseudoQueue()


queue.enqueue(5)
queue.enqueue(10)
queue.enqueue(15)
print(queue.dequeue())  # Output: 5
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 15
print(queue.dequeue())
