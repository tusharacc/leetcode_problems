# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
        
class ConvertToLinkedList:
    def __init__(self,number):
        self.number = number
        self.__convertToLinkedList()

    def __convertToLinkedList(self):
        number = self.number
        firstPass = True
        while True:
            q,r = divmod(number,10)
            number = q
            listNode = ListNode(r)
            if firstPass:
                self.head = listNode
                firstPass = False
            else:
                prev.next = listNode
            prev = listNode

            if q == 0:
                break
        

    def __str__(self):
        head = self.head
        temp = ""
        while head.next != None:
            temp +=  f"{head.val} "
            head = head.next
        temp +=  f"{head.val} "
        return temp
    
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    power = 0
    number1, number2 = 0,0
    while l1.next != None:
        number1 += pow(10,power)*l1.val
        power += 1
        l1 = l1.next
    number1 += pow(10,power)*l1.val
    power = 0
    number2 = 0
    while l2.next != None:
        number2 += pow(10,power)*l2.val
        power += 1
        l2 = l2.next
    number2 += pow(10,power)*l2.val
    return number2 + number1

if __name__ == '__main__':
    number1 = ConvertToLinkedList(342)
    print (number1)
    number2 = ConvertToLinkedList(465)
    print (number2)
    print (addTwoNumbers(number1.head, number2.head))