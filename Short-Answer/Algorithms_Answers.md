#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
The algorithm is basically calculating how long it takes for n^2 to reach n^3. 
The while loops ends when "a" reaches n^3. "a" is calculated by taking n^2 and adding it to itself for every loop.  In other words, a = 1 * n^2 for loop 1, a = 2 * n^2 for loop 2, a = 3 * n^2 for loop 3.... a = b * n^2 for loop b.

So the entire loop is simply multiplying n^2 by the number of times needed to reach n^3.

Therefore, the runtime is n^3 / n^2 = n.  So runtime is O(n).

b) 
The first loop in the algorithm is a simple for loop that iterates from 0 to n which means O(n) runtime.
The second (nested) loop is more complicated. It is a while loop that ends when j >= n where j starts from 1 and is multiplied by 2 each iteration. In other words, j = 2 ^ k where k = number of loops until j reaches n.  From this, we 
can say that the number of loops required as a function of n is:

log2(n) = k

So the runtime of the nested loop is log2(n).  Which means the overall runtime of both loops is O(n*log2(n)).


c) 
This algorithm is a simple recursive addition that adds 2 each time the function is called. Every time the function is called, the input "bunnies" is decreased by 1 until it reaches the base case of "bunnies" = 0.
In other words, the number of recursive loops or stages needed to reach the base case is simply how many times 1 must be subtracted from n to reach n = 0. Therefore, the number of recursive stages is n.  So the runtime of this algorithm is simply O(n)

## Exercise II
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.

## New Answer (old answer below)

(When I wrote my first answer I didn't see that they wanted us to minimize the number of broken eggs)

### Pseudocode 1 - Generic Recursive Binary Search
My initial answer had runtime O(n) because in the worst case, it checked every floor. To minimze number of eggs broken (number of loops/calls) we can use a Binary search.

The general function structure should look like:

def floor_finder(n, low = 0):
 - n is the highest floor and low is the lowest.

 - calculate the middle point (mid = (n+low) // 2)

check if we reach the base case (highest floor = lowest floor)
 - if n == low:
    return n

check if egg is broken by the HIGH floor
- if is_broken (n) == True:

        # f must be between mid and high
        return floor_finer(n, mid)


check if egg is broken by the MID floor
 - elif is_broken (mid) == True:
        
        # f must be between low and mid
        return floor_finder(mid, low)


What if egg is not broken by the highest floor?
  else:
        return "Get a taller building"


### Runtime complexity

This type of binary search cuts the search space in half with every call. The worst case scenario is when the break floor is at one of the extremes. In this case, the number of recursive calls required is 2 ^ k = n. Where k is number of calls. So we can rewrite the equation to get k = log2(n).  So the runtime is O(log2(n)).


### Pseudocode 2 (old)

A simple recursive solution would be to continually increment f until our egg breaks.

So our function would work like:

 - if f > n, then return None because we need a taller building

 - else: take f and use whatever physics formula to check if egg breaks

 - BASE CASE: if break == true:
    - Then return f

 - else: If break == False:
    - Then call function with f += 1


def floor_finder(f, n):

    if f > n:
        return None

    else:
        break = egg_drop_formula(f)

    if break == True:
        return f

    else:
        return floor_finder(f+1 ,n)

### Time Complexity

This solution repeatedly increments f by 1 and checks for egg break until the break condition is satisfied at which point, f is returned.

The worst possible runtime is when the function calls itself until f = n. Since we increment f by 1 for each call, this means that the max number of calls is n.  So our runtime is O(n)