class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 25: 
            return ascii_lowercase[columnNumber-1].upper()
        
        cn = columnNumber
        # while cn >= 25: 
        #     pass

        # use ord() method ? 

        return "a"
    



class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            result = chr(65 + remainder) + result
        return result