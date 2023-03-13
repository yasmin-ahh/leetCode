class Solution:
    def climbStairs(self, n: int) -> int:
        count = 1
        ll = [1]
        for i in range(1, n):
            ll.append(count)
            count += ll[i-1]
        return count 
