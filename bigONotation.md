# Big O Notation

*	[Introduction](#introduction)
*	[What is Big O used for](#what-is-big-o-used-for)
*	[How to test for Big O](#how-to-test-for-big-o)
*	[Tasks](#tasks)


## Introduction

Big O Notation is a way to classify the efficiency of a given program based on whatever part of the program takes the longest. 

Say you are at the end of a line of 400 people at Disney World. The ticket collector checking your tickets can only check one person at a time. For this kind of process the ticket collector would have to check every single person ahead of you before he got your ticket. Sorry no way to skip the line. Since we are doing the same check for each and every person in the list  and the endthis will result in an O(n) operation.

To keep things simple I will just talk about four different different types of Big O Notation.

**Big O of 1 or O(1)** means that no matter the size of your data it takes the same time to  get the result. This is know as **constant**.

**Big O of N or O(n)** this means that the performance or time it takes grows linearly as the data grows. This is like the example I gave in the introduction. The longer your line the longer your wait. This is known as **linear**.

**Big O of log of N or O(log(n))** means that the amount you have to look through gets cut shorter by each comparison. Each time that you do a check your data set gets smaller. A good example of this is a binary search (look it up!). This is known as **logarithmic**.

**Big O of n N to the power of x of O(n^x)** means that your performance gets worse or takes longer as the data size grows. This is worse than linear because the change in performance is exponential. This is like if you had to check if any person in a line has the same ticket as you, it could be even worse. That example is an O(n^2) performance.
This type of performance is known as **polynomial**.


## What is Big O used for

Your **Big O** is used to determine the performance of a given program. You want to have the best perfromance you can for a program and so the ideal situation would be where no matter the size of your data it always takes the same amount of time to  get the result you are looking for, an O(1) performance.


## How to test for Big O
It is important that you know how to figure out how to test for the Big O of an algortithm. Here is an example using python code:

```python
disney_ride_line = ["John", "Mary", "David", "Suzie", "Mike", "George"]

# If you are George, will it take longer to get to you than it would if you were John?

# Look at each person in the line starting at the beginning until you find George.
for person in disney_ride_line:
    if person == "George":
        print("Found George!")
```
Since we are looking for George and we are starting at the beginning of the line, we will have to check each one until we find George. This is an O(n) operation. The key thing to look for is the **loop**. If there is a loop and it goes through each item in your data set than it will have an O(n) performance.

If you run through the data set using a nested loop this would usually cause an O(n^2) or O(n^x), x being the amount of nested loops you have. This is supposing that for each loop you are using the same data set. Here is an example of that written in python:
```Python
disney_ride_line = ["John", "Mary", "David", "Suzie", "Mike", "George"]

# We are going to check if there is any person with the same name in our line.

for i in range(len(disney_ride_line)):
    person = disney_ride_line[i]

    for j in range(len(disney_ride_line)):
        person_two = disney_ride_line[j]

        # Don't check if i is the same number as j because that means that you are check the person with themselves.

        if i != j:
            if person == person_two:
                # If there is another person with the same name in the line then print it out. Otherwise print nothing.
                print(f"There is another {person} in the line.")

```
Because we are running through two loops, one nested inside of the other, and the size of the data set is not decreasing this will result in an O(n^2) performance.

## Tasks:

Task 1: What do you think the performance of this code would be:

```Python
disney_ride_line = ["John", "Mary", "David", "Suzie", "Mike", "George"]

# Print out the last item in the index
print(disney_ride_line[-1])
```

Task 2: What do you think the performance of this code would be:

```Python
disney_ride_line = ["John", "Mary", "David", "Suzie", "Mike", "George"]


for person in disney_ride_line:
    for letter in person:
        print(letter)
    print("------------")
```

Check your answers [here](bigONotationTaskAnswers.md) after you have tried to figure out the answer for yourself.