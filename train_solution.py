
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
        Insert a new wagon at the front (i.e. the locomotive) of the
        Train.
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

    def insert_caboose(self, value):
        """
        Insert a new wagon at the back (i.e. the caboose) of the 
        Train.
        """
        # Create the new wagon
        new_wagon = Train.Wagon(value)  
        
        # If the train is empty, then point both locomotive and caboose
        # to the new wagon.
        if self.caboose is None:
            self.locomotive = new_wagon
            self.caboose = new_wagon
        # If the train is not empty, then only self.caboose will be
        # affected.
        else:
            new_wagon.prev = self.caboose # Connect new wagon to the previous locomotive
            self.caboose.next = new_wagon # Connect the previous locomotive to the new wagon
            self.caboose = new_wagon   

    def remove_locomotive(self):
        """ 
        Remove the first wagon (i.e. the locomotive) of the train.
        """
        # If the train has only one item in it, then set locomotive and caboose 
        # to None resulting in an empty train.  This condition will also
        # cover an empty train.  Its okay to set to None again.
        if self.locomotive == self.caboose:
            self.locomotive = None
            self.caboose = None
        # If the train has more than one item in it, then only self.locomotive
        # will be affected.
        elif self.locomotive is not None:
            self.locomotive.next.prev = None  # Disconnect the second wagon from the first wagon
            self.locomotive = self.locomotive.next  # Update the locomotive to point to the second wagon

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

    def remove(self, value):
        """
        Remove the first wagon that contains 'value'.
        """
        # Look for the first wagon that matches value

        # Start your search at the locomotive
        curr = self.locomotive
        # Loop through the tain until you get to the caboose in # which case if you haven't found it end the loop
        while curr != None:
            if curr.cargo == value:
                # If the value is at the locomotive then we can just use our pre-written code to remove_locomotive()
                if curr == self.locomotive:
                    self.remove_locomotive()
                    break
                
                # Else if the value is at the caboose of the train then use remove_caboose()
                elif curr == self.caboose:
                    self.remove_caboose()
                    break
                # Otherwise if the value is anywhere else we will need to disconnect the current wagon and attach it previous and next to each other
                else:
                    # Set the current wagon's prevous's next to the current wagon's next
                    curr.prev.next = curr.next
                    # Set the current wagon's next's previous to the current wagon's previous
                    curr.next.prev = curr.prev
                    break
            else:
                # Go to the next wagon
                curr = curr.next
            
                
    def replace(self, old_value, new_value):
        """
        Search for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        # Start at the locomotive
        curr = self.locomotive
        # Loop until you have reached the caboose
        while curr != None:
            # If you have found the old value replace it 
            # with the new value
            if curr.cargo == old_value:
                curr.cargo = new_value
            else:
                # Otherwise go to the next wagon
                curr = curr.next
            
        pass

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


# TASK 1
t = Train() # Initialize the train
# Insert from the locomotive
t.insert_locomotive(1)
t.insert_locomotive(3)
t.insert_locomotive(5)
print(t) # Expected output Train[5]<->[3]<->[1]

# Insert from the caboose
t.insert_caboose(6)
t.insert_caboose(4)
t.insert_caboose(2)
print(t) # Expected output 
# Train[5]<->[3]<->[1]<->[6]<->[4]<->[2]

# TASK 2
# Remove from the locomotive
t.remove_locomotive()
t.remove_locomotive()
print(t) # Expected output Train[1]<->[6]<->[4]<->[2]

# Remove from the caboose
t.remove_caboose()
t.remove_caboose()
print(t) # Expected output 
# Train[1]<->[6]

# TASK 3
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
