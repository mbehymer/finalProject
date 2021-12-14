class BST:
    """
    This BST, binary search tree data structure uses a node class inside of it.
    You will call BST.Node to create a node. All of the attributes are inside of the Node class, while all of the methods are found in the BST class.
    """

    class Node:
        """
        This node class, it has a left, right and value
        """
        def __init__(self, value):
            
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):

        self.root = None
    
    def insert(self, value):
        """
        Put the value into the BST. As a special case if the BST is empty we will set the root equal to a new node and put the value in that. If it is empty then we will recursively look for a  place to put the value.
        """
        if self.root == None:
            self.root = BST.Node(value)
        else:
            self._insert(value, self.root) # Initiate the recursive function starting at the root.

    def _insert(self, value, node):
        """
        Recursively look for a place to put the node with the value in it. Here node is the subtree we are looking at. 
        """
        if value == node.value:
            # If the value is already in the tree then 
            # get out of the function
            return
        elif value < node.value:
            # The value will go to the left.
            if node.left == None:
                # This means we can place it here
                node.left = BST.Node(value)
            else:
                # Keep looking recursing down the left subtree
                self._insert(value, node.left)

        else:
            if node.right == None:
                #Yay we found an empty spot
                node.right = BST.Node(value)
            else:
                # Keep looking recursing down the right subtree
                self._insert(value, node.right)

    def __contains__(self, value):
        """ 
        Look to see if value is in the BST
        This is like saying:
        4 in my_bst
        """
        return self._contains(value, self.root)  # Start at the root

    ################
    # Begin Task 1 #
    ################
    def _contains(self, value, node):
        """
        This checks if your BST contains value.
        this is to be used by __contains__
        """
        # If it is in the current node then return the node
        if value == node.value:
            return True
        elif value < node.value:
            if node.left is not None:
                return self._contains(value, node.left) # Check if the value is in the left subtree
        else:
            if node.right is not None:
                return self._contains(value, node.right) # Check if the value is in the right subtree

        # If you couldn't find it using the previous cases return False
        return False
    ##############
    # END Task 1 #
    ##############
    
    def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.  This is called a generator function.
        This function is called when a loop	is performed:

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
    
    ################
    # Begin Task 2 #
    ################
        
    def _traverse_forward(self, node):
        """
        This moves forward though the bst yielding the 
        value in the node after doing a funciton to traverse 
        from the left we will be starting with the lowest 
        numbers first then we will do it from the right side

        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.value
            yield from self._traverse_forward(node.right)
        
    ##############
    # END Task 2 #
    ##############


    def __reversed__(self):
        """
        Perform a backward traversal this will call the  _traverse_backward fuction

        for value in reversed(my_bst):
            print(value)

        """        
        yield from self._traverse_backward(self.root)  # Start at the root

    def _traverse_backward(self, node):
        """
        This moves backward though the list and because we are yielding the value in the node after doing a funciton to traverse from the right we will be starting with the largest numbers first then we will do it from the left side

        This function is to be called by the __reversed function__        
        """
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.value
            yield from self._traverse_backward(node.left)

    
    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    ################
    # Begin Task 3 #
    ################
    def _get_height(self, node):
        """
        Figure out the height of the BST. You will add 1
        to whichever subtree is bigger, be that the right or to the left.
        A hint for this task is that you may want to think about comparing the left side with the right side to see which is bigger so keep track of their values.
        """
        heightR = 0
        heightL = 0
        height = 0
        if node.left is None and node.right is None:
            
            return 1
        else:
            if node.left is not None:
                heightL = self._get_height(node.left) + 1
            if node.right is not None:
                heightR = self._get_height(node.right) + 1

        if heightL > heightR:
            height = heightL
        else:
            height = heightR

        return height

    ##############
    # END Task 3 #
    ##############


t = BST()
t.insert(9)
t.insert(10)
t.insert(12)
t.insert(1)
t.insert(8)
t.insert(6)

# Task 1
print("Task 1")
print(9 in t) # True
print(7 in t) # False
print(1 in t) # True
print(13 in t) # False
print(14 in t) # False
print(6 in t) # True

# Task 2
print("Task 2")
for x in t:
    print(x) # 1 6 8 9 10 12


# Task 3
print("Task 3")
print(t.get_height()) # 4
t.insert(12)
print(t.get_height()) # 4
t.insert(5)
print(t.get_height()) # 5



