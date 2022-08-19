"""
  There is a programming language with only four operations and one variable X:

  ++X and X++ increments the value of the variable X by 1.
  --X and X-- decrements the value of the variable X by 1.
  Initially, the value of X is 0.

  Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
"""


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        def _op(term, n):
            match term:
                case "++X":
                    n += 1
                case "X++":
                    n += 1
                case "--X":
                    n -= 1
                case "X--": 
                    n -= 1
            return n
                
        out = 0
        for o in operations: 
            out = _op(o, out)
            
        return out