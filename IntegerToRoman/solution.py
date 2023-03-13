class Solution:
    def intToRoman(self, num: int) -> str:
        RomanNumerals = [["I", 1],["IV", 4], ["V", 5],["IX", 9], ["X", 10],["XL", 40],["L", 50],["XC", 90],["C", 100],["CD", 400],["D", 500],["CM", 900],["M", 1000]]
        pointerNumeral = len(RomanNumerals)-1
        finalString = ""
        while num > 0: 
            if num>= RomanNumerals[pointerNumeral][1]: 
                finalString = finalString+ RomanNumerals[pointerNumeral][0]
                num = num - RomanNumerals[pointerNumeral][1]
            else: 
                pointerNumeral -= 1
        return finalString
