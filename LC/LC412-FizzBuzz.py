class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range((n+1)):
            print(i)
            if i == 0: continue
            if i % 3 == 0 and i % 5 == 0:
                out.append("FizzBuzz")
                continue
            if  i % 3 == 0:
                out.append("Fizz")
                continue
            if i % 5 == 0:
                out.append("Buzz")
                continue
            out.append(str(i))
        return out
            