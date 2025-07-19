class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0) #Creates a ListNode object with val = 0 and next = None
        current = head #Copy the head to the current for further operation
        carry = 0 #Initialise carry with 0
        
        while l1 or l2: #For further operations until l1 or l2 becomes null
            val1 = l1.val if l1 else 0  #stores value of l1 into val1 if l1 is not 0
            val2 = l2.val if l2 else 0  #stores value of l2 into val1 if l2 is not 0
            total = val1 + val2 + carry  #Sum the values of the two list with carry
            carry = total // 10  #update carry with the left digit of the value(sum)
            current.next = ListNode(total % 10) # It creates new node with the right digit from sum as its value  (ex - total = 15 then Listnode(5))
            current = current.next #stores Newly created Node in current variable
            
            if l1:
                l1 = l1.next #If l1 is not None, move l1 to the next node
            if l2:
                l2 = l2.next #If l2 is not None, move l2 to the  next node
        
        if carry:
            current.next = ListNode(carry) # If any carry reamins then it creates a NewNode with carry as its value

        return head.next # returns the output linked list