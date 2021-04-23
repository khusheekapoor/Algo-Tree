"""
Problem Statement:
Add implementation of queue in Python.

Queue: A queue is a linear data-structure where elements can be inserted and deleted from both the ends.

A queue has the following properties.

• It is opened at both the ends.

• The end at which elements are addded in a queue is called the rear/back/tail.

• The end from which elements are removed from the queue is called head/front.

• Queue follows FIFO/LILO methodology to insert/remove elements.

• Unlike lists/arrays, queues don't allow for random access to the elements.

Main Operations in Queue:
• Enqueue: Used to add items to the queue. If the queue is full, it is a condition of the Queue Overflow. Time complexity: O(1).

• Dequeue: Used to remove an element from the queue.If the queue is empty, it is a condition of the Queue Underflow. Time complexity: O(1).

• Front/Peek: Displays an element from the front end. Time complexity: O(1).

• Rear: Displays an element from the rear end. Time complexity: O(1).

• isEmpty: Returns True if the Queue is empty, otherwise, False.
"""


class queue:
    def __init__(self):
        self.__queue = []
        self.__size = 0

    def enqueue(self, data):
        """ adds items to the queue """
        self.__queue.append(data)
        self.__size += 1

    def dequeue(self):
        """ remove items from the queue """
        if not self.isEmpty():
            element = (self.__queue[0])
            self.__queue.remove(element)
            self.__size -= 1
            print(element, "has been removed")
            return

    def front(self):
        """ displays an item from the front end """
        print("Front element is:", self.__queue[0])
        return

    def rear(self):
        """ displays an item from the rear end """
        print("Rear element is :", self.__queue[-1])
        return

    def isEmpty(self):
        """ returns true if the queue is empty """
        return self.__size == 0

    def display_queue(self):
        """ displays the queue """
        if self.isEmpty():
            print("The queue is empty")
            return
        for i in self.__queue:
            print(i, "--->", end=' ')
        print(None)

"""Time-Complexity:
enqueue(): O(1)
dequeue(): O(1)
front(): O(1)
rear(): O(1)
isEmpty(): O(1)
display_queue(): O(N)
"""


if __name__ == "__main__":
    q = queue()
    q.display_queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.display_queue()
    q.dequeue()
    q.dequeue()
    q.front()
    q.rear()
    print(q.isEmpty())

"""Expected Output:

The queue is empty
10 ---> 20 ---> 30 ---> 40 ---> None
10 has been removed
20 has been removed
Front element is: 30
Rear element is : 40
False
"""
