#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
    Linear,there is just one loop

b) O(n^2)
    Polynomial, there is a nested while loop in the for loop 

c) O(n)
    Linear, no loop 

## Exercise II

1. Find the middle floor by spliting the length of the amount of stories in the building
2. Drop an egg
    a. if it breaks, go down one floor, drop another egg

            if the egg does not break, subtract the dropped eggs(plus one) from the middle floor, this will return floor f.

            else if the egg does break, repeat step a

    b. else if it does not break, go up one floor, drop another egg

            if the egg breaks add number of dropped eggs to the middle floor, this will retrun floor f
            
            else if the egg does not break, repeat step b

I think this solution would be O(n) becasue n would be constant and I dont think there 
    would be a nested loop


