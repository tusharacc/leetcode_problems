'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''

from typing import List
class Solution:
    def helper(self,end:int,steps:List[int]):  
        if self.lastStep.get(end,0):
            return self.lastStep[end]
        if end == 0:
            return 1
        elif end < 0:
            return  0
        else:
            result = 0
            for step in steps:
                result += self.helper(end-step,steps)
            self.lastStep[end] = result
            return self.lastStep[end]

    def climbStairs(self, n: int) -> int:
        self.lastStep = {}
        self.helper(n,[1,2]) 
        return self.lastStep[n]     

if __name__ == '__main__':
    solution: Solution = Solution()
    print(solution.climbStairs(4)  )
    
