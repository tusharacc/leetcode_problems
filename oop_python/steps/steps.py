'''
There is a staircase with n steps. A person standing at the 0-th step wants to reach the n-th one. 
They are capable of jumping up by certain numbers of steps at a time.

Given how the person can jump, count the number of ways they can reach the top.

{
"steps": [1, 2],
"n": 1
}
'''

from typing import List

score = 0
def helper(start:int, end:int,steps:List[int]):
    global score
    for step in steps:
        if start+step < end:
            helper(start+step,end,steps)
        elif start + step == end:
            score += 1
            return 
        else:
            return 0

def count_ways_to_climb(steps, n):
    """
    Args:
     steps(list_int32)
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    global score
    score = 0 
    helper(0,n,steps)
    return score

if __name__ == '__main__':
    count = count_ways_to_climb([2,3],7)
    assert count == 3, f"Incorrect Value {count}"

    count = count_ways_to_climb([1,2],1)
    assert count == 1, f"Incorrect Value {count}"

    count = count_ways_to_climb([1,2],2)
    assert count == 2, f"Incorrect Value {count}"

    count = count_ways_to_climb([2,3,5],10)
    assert count == 14, f"Incorrect Value {count}"

    count = count_ways_to_climb([41, 8, 2, 44, 9, 25, 24, 43, 31, 26, 21],105)
    assert count == 1386843059, f"Incorrect Value {count}"