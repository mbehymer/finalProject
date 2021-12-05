# QUEUE
*	[Introduction](#introduction)
*	[What are Queues used for](#what-are-queues-used-for)
*	[Big O of Queues](#big-o-of-queues)
*	[Example](#example)
*	[Problem to Solve](#problem-to-solve)


## Introduction
Queues are like a list of items or people in a line. They follow and have an order into they way they are put in and taken out which goes as First In, First Out (FIFO). 
![Queue of a line of people at Disney Land](queue_disney_land.png)
Say that our queue is like a line of people at Disney Land. The first person in the line is the first one to be admitted onto the ride or into Disney Land, this is the same way that a queue works.

## What are Queues used for
Queues are used when you want to do something in the order that you received them or FIFO. Say your at Disney Land and you want to buy a churro. The first person in the line is going to be the first one to get a churro. You will have to wait until you are the first person in the line. 
Anyhting that goes in this order, FIFO, you would want to use a queue.

## Big O of Queues
Alrighty well now you know a little more about what a line at Disney Land is actually called, a queue. But we need to talk about it's performance.

When you add to your queue or when you enqueue your queue you don't need to change you queue, nothing needs to be shifted around. All you have to do is put it on the end of your queue. So the Big O of enqueueing would be O(1). Now say you want to remove an item. To do so you would take everything that comes before it and shift it forward one, this is because it follows the FIFO rule. 

Say the person in the middle of the line decides he wants to go on a different ride. He gets out of the line, but now the line has to update, everyone before the guy in the middle will have to move forward by one. So the Big O of dequeueing will be O(n) because you have to update and shift everything that came after that item one to the left. So to summarize to enqueue is O(1) and dequeue is O(n). So in python a queue is like a list.

## Example
Here is some sample code for you to follow on how to make a Disney Land line, or rather a queue:
```Python
class DisneyLandLine:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, person):
        # Add a person to the end of the queue
        # Todo
        pass

    def dequeue(self):
        # Remove the first person from the queue
        # Todo
        pass
```

## Problem to Solve
Use the code above to solve these problems to make sure that you correctly made a queue using the sample code above and the problems below.

### Task 1:
```Python
my_line = DisneyLandLine()
my_line.enqueue("John")
my_line.enqueue("Mark")
my_line.enqueue("Susan")

# Expectation return ['John', 'Mark', 'Susan']
print(my_line.queue)
```

### Task 2:
Using the previous code block:

```Python

my_line.dequeue()
my_line.dequeue()
my_line.dequeue()
my_line.dequeue()
# Expectation should remove everything from the queue and if there is nobody in the queue, it should let the user know that there is no one in the queue.
print(my_line.queue)
```

Check your answers [here](queueTaskAnswers.md) after you have tried to figure out the answer for yourself.