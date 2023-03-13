class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0 
        if n>3: 
            prime = [True for i in range(n)]
            p = 2
            while (p * p <= n):
                if (prime[p] == True):
                    for i in range(p * p, n, p):
                        prime[i] = False
                p += 1
                
            for p in range(2, n):
                if prime[p]:
                    count = count +1

            return count
        else: 
            if n == 3: 
                return 1
            else: 
                return 0
