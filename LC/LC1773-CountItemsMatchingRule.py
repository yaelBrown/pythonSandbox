"""
You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.
"""


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        rk = 0
        match ruleKey:
            case "type": 
                rk = 0
            case "color":
                rk = 1
            case "name": 
                rk = 2

        for i in items: 
            if ruleValue == i[rk]: 
                cnt += 1
            
        return cnt
