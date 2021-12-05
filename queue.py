class DisneyLandLine:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        # Add to the end of the list
        self.queue.append(data)

    def dequeue(self):
        # Remove the first item from the list
        if len(self.queue) >= 1:
            self.queue.pop(0)
        else:
            print("There are no items in your list.")
            
my_line = DisneyLandLine()
my_line.enqueue("John")
my_line.enqueue("Mark")
my_line.enqueue("Susan")

print(my_line.queue)


my_line.dequeue()
my_line.dequeue()
my_line.dequeue()
my_line.dequeue()

print(my_line.queue)

