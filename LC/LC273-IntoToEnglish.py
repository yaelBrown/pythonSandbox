class Solution(object):
    def numberToWords(self, num):
        # https://leetcode.com/problems/integer-to-english-words/discuss/70632/Recursive-Python
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def words(n):
            if n < 20:
                return to19[n - 1:n]
            if n < 100:
                return [tens[n / 10 - 2]] + words(n % 10)
            if n < 1000:
                return [to19[n / 100 - 1]] + ['Hundred'] + words(n % 100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (p + 1):
                    return words(n / 1000 ** p) + [w] + words(n % 1000 ** p)
        return ' '.join(words(num)) or 'Zero'
    


# Generate words map, add words into an array, join the array. return the array or Zero.


class Solution:
    def numberToWords(self, num: int) -> str:
        numMap = {
            0: "Zero",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            20: "Twenty",
            30: "Thirty",
            40: "Fourty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }

        s, t, o = str(n), n, ""

        _ = n / 1000000000    
        if _ >= 1:
            o += numMap[int(_)] +  numMap[1000000000] + " "

        #? 

