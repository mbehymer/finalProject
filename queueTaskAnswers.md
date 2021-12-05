```Python
class DisneyLandLine:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, person):
        # Add to the end of the list
        self.queue.append(person)

    def dequeue(self):
        # Remove the first person from the queue
        if len(self.queue) >= 1:
            self.queue.pop(0)
        else:
            print("There are no people in your line.")
            
my_line = DisneyLandLine()
my_line.enqueue("John")
my_line.enqueue("Mark")
my_line.enqueue("Susan")

# Expectation return ['John', 'Mark', 'Susan']
print(my_line.queue)


my_line.dequeue()
my_line.dequeue()
my_line.dequeue()
my_line.dequeue()

# Expectation should remove everything from the queue and if there is nobody in the queue, it should let the user know that there is no one in the queue.
print(my_line.queue)
```