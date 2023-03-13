import re
class Solution:
  
    def myAtoi(self, s: str) -> int:
        # Initialize empty string to store numbers in
        strTemp = ""

        #Loop over chars in string 
        for i in s: 
            # Condition if there is a whitespace and it is still in the begining of the string 
            # This is assumed when there are no elements added yet to the string 
            if i == " " and len(strTemp) == 0: 
                continue 
            #if we meet a + or a - before any numbers 
            elif (i == "-" or i == "+") and len(strTemp) == 0: 
                strTemp += i 
            # if we meet a digit then we append it to the string 
            elif i.isdigit() :
                strTemp += i
            # If non of those coditions are met then we stop the loop 
            else: 
                break 

        if not re.search("[0-9]", strTemp[0:]):
            return 0 
        if int(strTemp) <= pow(-2, 31): 
            return pow(-2, 31)
        if int(strTemp) >= pow(2, 31)-1: 
            return pow(2, 31)-1
        else: 
            return int(strTemp)
