l1 = [2,4,3]
l2 = [5,6,4]

class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = ''
        num2 = ''
        l3 = []
        final_list = []
        for i in range(len(l1)):
            popped = l1.pop()
            num1 += str(popped)  
        for j in range(len(l2)):
            popped = l2.pop()
            num2 += str(popped) 
        total = int(num1)+int(num2)
        for k in str(total):    
            l3.append(int(k))
        for l in range(len(l3)):
            popped = l3.pop()
            final_list.append(popped)
        print(final_list)
        
if __name__ == "__main__":
    solution = Solution()
    solution.addTwoNumbers(l1, l2)