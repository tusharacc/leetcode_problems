'''
Given some balls of three colors arranged in a line, rearrange them such that all the red balls go first, then green and then blue ones.

Do rearrange the balls in place. A solution that simply counts colors and overwrites the array is not the one we are looking for.

This is an important problem in search algorithms theory proposed by Dutch computer scientist Edsger Dijkstra. Dutch national flag has three colors (albeit different from ones used in this problem).
[r,r,...,g,g...,b,b]
'''

def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    lo: int = 0
    mid: int = 0
    hi: int = len(balls) - 1

    while mid <= hi:
        if balls[mid] == 'R':
            balls[lo],balls[mid] = balls[mid],balls[lo]
            lo += 1
            mid += 1
        elif balls[mid] == 'G':
            mid += 1
        else:
            balls[mid] == 'B'
            balls[hi], balls[mid] = balls[mid], balls[hi]
            hi -= 1
    
    return balls

if __name__ == '__main__':
    balls =  ["G", "B", "G", "G", "R", "B", "R", "G"]
    print(dutch_flag_sort(balls))
        

