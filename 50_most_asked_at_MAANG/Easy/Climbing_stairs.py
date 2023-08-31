'''
Climbing stairs

You are climbing a staircase, it takes n steps to reach the top 

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 

Example 
Input n = 2
output 2 
Explanation - there are two ways to climb to the top 
    1. 1 step + 1 step 
    2. 2 steps 

'''


# easiest way is to implement the fibonacci sequence 
def climbStairs(n:int) -> int:
    
    one, two = 1, 1 

    for i in range(n-1):
        temp = one 
        one = one+two
        two = temp 
    
    return one

n = 4

print(climbStairs(n))