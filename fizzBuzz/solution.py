class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        store1 = []
        for i in (range(1,n+1)): 
            print(i)
            if i%3 == 0 and i%5 == 0: 
                store1.append("FizzBuzz")
            elif i%3 == 0: 
                store1.append("Fizz")
            elif i%5 == 0: 
                store1.append("Buzz")
            else: 
                store1.append(str(i))
        return store1
