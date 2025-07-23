class Solution:
    def reverse(self, x: int) -> int: 
        if '-' in str(x):
            if -2**31 <= int('-' + str(x)[1:][::-1]) <= 2**31 - 1:
                return int('-' + str(x)[1:][::-1])
            else:
                return 0
        
        elif '0' in str(x) and ((int(str(x)[::-1])) < 2**31) and (-2**31 <= x <= 2**31 - 1) :
                return int(str(x)[::-1])    
            
        else:
            if ((int(str(x)[::-1])) < 2**31) and (-2**31 <= x <= 2**31 - 1):
                return int(str(x)[::-1])
            else:
                return 0