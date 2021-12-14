# LINKED LISTS
*	[Introduction](#introduction)
*	[How do Linked Lists Work](#how-do-link-lists-work)
*	[Big O of Linked Lists](#big-o-of-linked-lists)
*	[Example](#example)
*	[Problem to Solve](#problem-to-solve)

## Introduction
With queues everything followed a specific order. Like python lists, they are indexed and you can easily jump to which ever one if you know the index. Linked lists are different, they are not organized into a nice line where you can grab any given one by simply saying the index. Rather the way a linked list works is you have a bunch of nodes and those nodes three things. They contain a link to the next node, a link to the previous node and the data that has been assigned to the given node.

The other thing to note is that a linked list always has a head, the beginning, and it has a tail, the end. A good way to think about lists are like trains. There is the locomotive (head of the train) and the caboose (tail of the train). Each wagon contains people or cargo and each is connected to the next wagon and the previous wagon.
![Linked List Train](linked_list_train.png)
Since there is nothing that comes before the head, the locomotive, the previous of the head is always set to None in python. For the tail, the caboose, the opposite is true, there is nothing that comes after the coboose so next is always set to None as well.

Say we start out with no train. Our Locomotive is set to None, and so is the caboose. Now lets say we want to add some things to our train. We can insert from either the locomotive or the caboose. In python this would look something like this if we had a class Train:
```Python
my_train = Train() # Currently the head and the tail don't have anything in them so everything is set to None.

print(my_train) # Result Train[]
my_train.insert_caboose(3)
print(my_train) # Result Train[3]
my_train.insert_caboose(2)
print(my_train) # Result Train[3]<->[2]
my_train.insert_locomotive(1)
print(my_train) # Result Train[1]<->[3]<->[2]
my_train.insert_locomotive(5)
print(my_train) # Result Train[5]<->[1]<->[3]<->[2]
```

## How do Linked Lists Work

### Insert From the Caboose
Our first insert in this case from the caboose would set the caboose and locomotive both equal to three because if we only have one wagon on the train then it is both the locomotive and the caboose. Next when we insert again from the caboose, the caboose now changes to the value 2 and the locomotive stays as the value 3. These are the steps you would take:
1. You will need to add a new wagon (node).
2. Set the new wagon's previous to the caboose, which is also the locomotive in this case.
3. Now set the caboose's next equal to the new wagon. 
4. Finally you will set the caboose equal to the new wagon.

![Caboose insert](linked_list_train_caboose_insert.png)

### Insert From the Locomotive
When you insert from the locomotive it is pretty much the same, but I'll give you the steps.

1. You will need to add a new wagon (node).
2. Set the new wagon's next to the locomotive.
3. Now set the locomotive's previous equal to the new wagon. 
4. Finally you will set the locomotive equal to the new wagon.

This is all fine and dandy if you just want to add to one end or the other, but how would you insert something at a given index? Say from our code above we want to insert a 9 after the wagon holding a 1. This is what the code would look like:
```Python
# Assume this is our train -> Train[5]<->[1]<->[3]<->[2]

# Insert a wagon with a cargo value of 9 after the wagon with the cargo of value 1

my_train.insert_after(1, 9) 
print(my_train) # Result Train[5]<->[1]<->[9]<->[3]<->[2]

```
### Insert After a Given Cargo
How this works is different than how you would insert in a list in pyhon. Since you can't just go to the index that contains 1 you will have to loop through each one until you found the correct value. If the value wasn't in the train then you would need to notify the user once the loop got to the caboose.

Now once you find the value you are looking for these are the steps you would take to insert it. Let's call the wagon you are inserting the new wagon after current.
1. Create a new wagon.
2. Connect the new wagon's previous to the current wagon.
3. Connect the new wagon's next to the current wagon's next.
4. Set the current wagon's next's previous to the new wagon.
5. Set the current wagon's next to the new wagon.

This is what it would look like:
![Inserting After For a Train](linked_list_train_insert_after.png)

Okay, now we now how to put stuff on our train, but what about if we want to remove from our train?

### Removing From the Caboose
If we ant to remove the caboose from the train the process would be pretty simple. Here is what we would do:
1. Set the caboose equal to the caboose's previous.
2. Now set caboose's next to None.

Since we don't care what happens to whatever the caboose was we can just disconnect it.

### Removing From the Locomotive
The process of removing from the locomotive is pretty much the same as removing frmo the caboose:
1. Set the locomotive equal to the locomotive's next.
2. Now set the locomotive's previous to None.

You would need to make sure that if the wagon you are removing is the last wagon, then set the locomotive and the caboose equal to None.

### Removing From the Middle
Alrighty, so you can remove from the caboose and from the locomotive, but how would we do that if we wanted to remove a wagon from the middle?

To do so is not as complicated as inserting after. Here is what you would do after finding the wagon you want to remove. We'll call it the current wagon:
1. Set the current wagon's previous's next to the current wagon's next.
2. Set the current wagon's next's previous to the current wagon's previous.

That's only two steps, way less then inserting after.


## Big O of Linked Lists
Lets discuss the Big O notation of linked lists. 

**Finding a given Node**

Since nothing uses an index, you have to always start at the head (locomotive) or the tail (caboose). From there you will loop through each node (wagon) until you have found the one you are looking for. This means that, unless you are looking for the head or the tail, you will always have an O of n or O(n) when looking for a given node.

**Deleting or Inserting**

When you are trying to delete a wagon or when you are inserting the deletion/insertion will always be O(n) unless it is at the locomotive(head) or the caboose (tail) of your train (linked list). This is because you do not need to move any of the other wagons, you only need to link some wagons up.

Here is a table of how the big O looks:

Task | Description | Big O
---------------|-------------------|---------------
insert_locomotive(data) | Add a wagon (node) from the Locomotive end. | O(1)
insert_caboose(data) | Add a wagon (node) from the Caboose end. | O(1)
insert_after(i, data) | Add a wagon (node) after the specified wagon. | O(n)
remove_locomotive() | Remove the Locomotive. | O(1)
remove_caboose() | Remove the Caboose. | O(1)
remove_wagon(value) | Remove the wagon that has the specified value. | O(n)
size() | Every wagon is tracked so you know how many wagons there are. | O(1)
empty() | Check if size() is equal to 0 | O(1)

So the


## Example

Here is some example code. Use this when trying to solve the tasks below.

```Python

class Train:
    """
    Implement the Train data structure.  The Wagon class below is an 
    inner class.  An inner class means that its real name is related to 
    the outer class.  To create a Wagon object, we will need to 
    specify Train.Wagon
    """

    class Wagon:
        """
        Each wagon of the train will have cargo and links to the 
        previous and next wagon. 
        """

        def __init__(self, cargo):
            """ 
            Initialize the wagon to the cargo provided.  Initially
            the links are unknown so they are set to None.
            """
            self.cargo = cargo
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty Train.
        """
        self.locomotive = None
        self.caboose = None

    def insert_locomotive(self, value):
        """
        Insert a new wagon at the front (i.e. the locomotive) of the Train.
        """
        # Create the new wagon
        new_wagon = Train.Wagon(value)  
        
        # If the train is empty, then point both locomotive and caboose
        # to the new wagon.
        if self.locomotive is None:
            self.locomotive = new_wagon
            self.caboose = new_wagon
        # If the train is not empty, then only self.locomotive will be
        # affected.
        else:
            new_wagon.next = self.locomotive # Connect new wagon to the previous locomotive
            self.locomotive.prev = new_wagon # Connect the previous locomotive to the new wagon
            self.locomotive = new_wagon      # Update the locomotive to point to the new wagon

    ################
    # Start Task 1 #
    ################
    def insert_caboose(self, value):
        """
        Insert a new wagon at the back (i.e. the caboose) of the Train.
        """
        
        # Create the new wagon
        # TODO
        
        # If the train is empty, then point both locomotive and caboose
        # to the new wagon.
        # TODO

        # If the train is not empty, then 
        # only self.caboose will be affected.
        # TODO
        pass   

    ##############
    # End Task 1 #
    ##############

    ################
    # Start Task 2 #
    ################

    def remove_locomotive(self):
        """ 
        Remove the first wagon (i.e. the locomotive) of the train.
        """
        # If the train has only one item in it, then set locomotive and caboose 
        # to None resulting in an empty train.  This condition will also
        # cover an empty train.  Its okay to set to None again.
        # TODO

        # If the train has more than one item in it, then only self.locomotive
        # will be affected.
        # TODO
        pass

    ##############
    # End Task 2 #
    ##############

    def remove_caboose(self):
        """
        Remove the last wagon (i.e. the caboose) of the Wagon.
        """
        # If the train has only one item in it, then set locomotive and caboose 
        # to None resulting in an empty train.  This condition will also
        # cover an empty train.  Its okay to set to None again.
        if self.locomotive == self.caboose:
            self.locomotive = None
            self.caboose = None
        # If the train has more than one item in it, then only self.caboose
        # will be affected.
        elif self.caboose is not None:
            self.caboose.prev.next = None  # Disconnect the second wagon from the first wagon
            self.caboose = self.caboose.prev  # Update the locomotive to point to the second wagon

    def insert_after(self, value, new_value):
        """
        Insert new_value after the first time you see value in
        the train.
        """
        # Look for the wagon that matches value by starting at the 
        # locomotive of the train.
        curr = self.locomotive
        while curr is not None:
            if curr.cargo == value:
                # If 'value' is at the end of the train,
                # then we can call insert_caboose to add 'new_value'
                if curr == self.caboose:
                    self.insert_caboose(new_value)
                # If not then we need to create a 
                # new wagon and reconnect the train to insert the said wagon.
                else:
                    new_wagon = Train.Wagon(new_value)
                    new_wagon.prev = curr       # Connect new wagon to the wagon containing 'value'
                    new_wagon.next = curr.next  # Connect new wagon to the wagon after 'value'
                    curr.next.prev = new_wagon  # Connect wagon after 'value' to the new wagon
                    curr.next = new_wagon       # Connect the wagon containing 'value' to the new wagon
                return # We can exit the function after we insert
            curr = curr.next # Go to the next wagon to search for 'value'
    
    ################
    # Start Task 3 #
    ################
    def remove(self, value):
        """
        Remove the first wagon that contains 'value'.
        """
        # Look for the first wagon that matches value

        # Start your search at the locomotive
        curr = self.locomotive
        # Loop through the tain until you get to the caboose in # which case if you haven't found it end the loop
        # TODO
                # If the value is at the locomotive then we can just use our pre-written code to remove_locomotive()
                # TODO
                
                # Else if the value is at the caboose of the train then use remove_caboose()
                # TODO

                # Otherwise if the value is anywhere else we will need to disconnect the current wagon and attach it previous and next to each other
                # TODO
        pass
    ##############
    # End Task 3 #
    ##############

    def __iter__(self):
        """
        Iterate foward through the train
        """
        curr = self.locomotive  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.cargo  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the wagon

    def __reversed__(self):
        """
        Iterate backward through the train
        """
        curr = self.caboose # Start at the end
        while curr is not None:
            yield curr.cargo # Yield the value
            curr = curr.prev # Go backwards

    def __str__(self):
        """
        Return a string representation of the train.
        """
        output = "Train["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += "]<->["
            output += str(value)
        output += "]"
        return output

```


## Problem to Solve

Use the example code above and modify it to solve these tasks

### Task 1:
```Python
t = Train() # Initialize the train
# Insert from the locomotive
t.insert_locomotive(1)
t.insert_locomotive(3)
t.insert_locomotive(5)
print(t) # Expected output Train[1]<->[3]<->[5]

# Insert from the caboose
t.insert_caboose(6)
t.insert_caboose(4)
t.insert_caboose(2)
print(t) # Expected output 
# Train[1]<->[3]<->[5]<->[6]<->[4]<->[2]

```

### Task 2:
```Python

# Remove from the locomotive
t.remove_locomotive()
t.remove_locomotive()
print(t) # Expected output Train[5]<->[6]<->[4]<->[2]

# Remove from the caboose
t.remove_caboose()
t.remove_caboose()
print(t) # Expected output 
# Train[5]<->[6]

```


### Task 3:
```Python
# Insert 3 into the train after 1
t.insert_after(1, 3)
# Insert 5 into the train after 3
t.insert_after(3, 5)
# Insert 7 into the train after 5
t.insert_after(5, 7)
# Insert 9 into the train after 7
t.insert_after(7, 9)
print(t) # Expected output Train[1]<->[3]<->[5]<->[7]<->[9]<->[6]

# Remove 3, 5 and 9 from the train
t.remove(3)
t.remove(5)
t.remove(9)
print(t) # Expected output [1]<->[7]<->[6]

# What happens if nothing is inside the train?
t.remove_locomotive()
t.remove_locomotive()
t.remove_locomotive()
t.remove(1)
t.remove_caboose()
# Expected outcome nothing should happen, no errors

```

To see the answers go [here](train_solution.py) and run the code