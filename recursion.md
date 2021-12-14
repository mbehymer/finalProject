# RECURSION
*	[Introduction](#introduction)
*	[How to do Recursion](#how-to-do-recursion)
*	[Recursion Tasks](#recursion-tasks)

## Introduction
Recursion is when a function will call itself. You can think of this kind of as a loop. Here is an example:
```Python
def add_to_yourself(num):
    print(num)
    num += 1
    add_to_yourself(num)

add_to_yourself(0)
```
The code above will run until you get a **RecursionError** because there is nothing that breaks it out of the loop, rather it would loop forever if it could.

What can you do to fix this problem. To solve the problem of getting the **RecursionError** you will need to have a base case and often you will have multiple base cases.

To stop the code above from looping forever we can add a base case like this:
```Python
def add_to_yourself(num, endNum):
    # Base case get out of the loop if 'num' is equal to 'endNum'
    if num == endNum:
        return

    print(num)
    add_to_yourself(num + 1, endNum) # smaller problem

add_to_yourself(0, 10)
# Output: 0 1 2 3 4 5 6 7 8 9

```

There are two **IMPORTANT** rules to follow with recurion:
* You must have a smaller problem - We need to call our function on a smaller problem. Basically if the values never changed in the recursive function than it would loop forever.
* You must use (a) base case(s) - You need base cases to tell your program when to stop calling itself.

## How to do Recursion:

You might be thinking well I can do this with a for loop pretty easily and that is true, but there are many cases where it is much shorter to write a recursive function than it would be to do it with loops. Now in python loops will always be more efficient than using recursion, but recursion usually have a more easily understood solution.

To do recursion you need to first establish what are the base cases of your program,
```Python
    # Base case get out of the loop if 'num' is equal to 'endNum'
    if num == endNum:
        return
```
then from there you will need to apply your smaller problem
```Python
    print(num)
    add_to_yourself(num + 1, endNum) # smaller problem
```

**MEMOIZATION**:

Now there is another important part to know for doing recursion. You may need to improve the performance of your recursive function. Take this code for example:
```Python
def three_add_seq(num):

    if num <=3: #Base case
         return 1

    result = three_add_seq(num-1) + three_add_seq(num-2) + three_add_seq(num-1)
    
    return result

print(three_add_seq(5))
print(three_add_seq(10))
print(three_add_seq(20))
print(three_add_seq(50)) #This will take too long to run
```
The last line `print(three_add_seq(50))` will take a long time to run. But if we change the code so that it stores its previous results we can make the code run faster because it can look up the stored answer in a dictionary. This is **memoization**.


## Recursion Tasks
Use the code Below to solve the task.
```Python

def count_ways_to_swing(mb, remember = None):
    """
    Imagine you are on the monkey bars (mb) at a playground and
    you want to figure out the how many ways you can swing across
    all of the bars. If you can only swing from one bar to the
    next then the number of ways would always be one. But if you 
    could choose to swing between one two or three bars in any 
    order than the total number would be way more. If there are
    just four bars then the amount of choices would be as follows:
        
        1 swing, 1 swing, 1 swing, swing
        1 swing, 1 swing, 2 swings
        1 swing, 2 swings, 1 sing
        2 swings, 1 swing, 1 sing
        1 swing, 3 swings
        2 swings, 2 swings
        3 swings, 1 swing

	With just one bar to go, the ways to get
    to the end of 'mb' monkey bars is to either:
    
    - take a single swing from the second to last bar, 
    - take a double swing from the third to last bar, 
    - take a triple swing from the fourth to last bar

    We don't need to think about scenarios like taking two 
    single swings from the third to last bar because this
    is already part of the first scenario (taking a single
    swing from the second to last bar).

    These final leaps give us a sum:

    count_ways_to_swing(mb) = count_ways_to_swing(mb-1) + 
                             count_ways_to_swing(mb-2) +
                             count_ways_to_swing(mb-3)

    To run this function for larger values of 'mb', you will need
    to update this function to use memoization.  The parameter
    'remember' has already been added as an input parameter to 
    the function for you to complete this task.
    
    The last test case is commented out because it will not work
    until the memoization is implemented.
    """

    # Base Cases
    if mb == 0:
        return 0
    elif mb == 1:
        return 1
    elif mb == 2:
        return 2
    elif mb == 3:
        return 4

    # Solve using recursion
    else:
        
        ways = count_ways_to_swing(mb-1) + count_ways_to_swing(mb-2) + count_ways_to_swing(mb-3)
        
        return ways


# Test Cases
print(count_ways_to_swing(5)) # 13 
print(count_ways_to_swing(10)) # 274 
print(count_ways_to_swing(25)) # 2555757 
print(count_ways_to_swing(500))  # 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527 This will take too long with the current code
```

How do you fix the code so that it will work? After trying it out compare your answer with the solution [here](recursion_solution.py)