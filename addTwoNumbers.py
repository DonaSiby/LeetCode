"""
Created on Sat Feb 25 15:56:34 2023

@author: Dona Siby
"""
from typing import Optional
#Definition of a SinglyLinkedList
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
        
#Add Two Numbers - Leetcode Question 2 

class Solution2:
    def addTwoNumbers(self,l1:Optional[ListNode],l2:Optional[ListNode])->Optional[ListNode]:
        dummyHead=ListNode(0)  #defining a linkedList
        carry=0  #initializing carry to 0
        current=dummyHead  #current head starts from dummy head
        
        while l1 or l2 or carry:
            l1val=l1.val if l1 else 0 
            l2val=l2.val if l2 else 0

    # =============================================================================
    # The above line of code is similar to this block
    #------------------------------------------------------------------------------
    #         if l1:
    #             l1val=l1.val
    #         else:
    #             l1val=0
    # =============================================================================
            
            sums=l1val+l2val+carry
            carry=sums//10
            newNode=sums%10  #create a new node with the sum as its value
            current.next=ListNode(newNode)  #link the new node to the current node
            current=current.next  #updating the 'current' value
            
            #updating l1 and l2
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
            
        return dummyHead.next
        
#test case
l1=ListNode(2,ListNode(4,ListNode(3)))
l2=ListNode(5,ListNode(6,ListNode(4)))

s=Solution2()
result=s.addTwoNumbers(l1, l2)

#to print the result
while result:
    print(result.val,end="->")
    result=result.next

       
            
            
    
    
