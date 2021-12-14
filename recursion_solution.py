
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
    if remember == None:
        remember = dict()


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
        
        if mb in remember:
            return remember[mb]

        ways = count_ways_to_swing(mb-1, remember) + count_ways_to_swing(mb-2, remember) + count_ways_to_swing(mb-3, remember)
        
        remember[mb] = ways
        return ways

        

# Test Cases
print(count_ways_to_swing(5)) # 13 
print(count_ways_to_swing(10)) # 274 
print(count_ways_to_swing(25)) # 2555757 
print(count_ways_to_swing(500))  # 1306186569702186634983475450062372018715120191391192207156664343051610913971927959744519676992404852130396504615663042713312314219527
