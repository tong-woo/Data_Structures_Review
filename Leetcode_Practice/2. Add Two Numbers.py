"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

class ListNode:
    def __init__(self, value = 0, next = None):
        self.val = value
        self.next = next



class Solution(object):
    def addTwoNumbers(self, l1, l2):

        list1 = []
        list2 = []
        res = []
        resL = ListNode()
        carry = 0
        while(l1 != None):
            list1.append(l1.val)
            l1 = l1.next
        while(l2 != None):
            list2.append(l2.val)
            l2 = l2.next
        if len(list1) < len(list2):
            for i in range(len(list2)-len(list1)):
                list1.append(0)
        else:
            for i in range(len(list1)-len(list2)):
                list2.append(0)
        for digit1, digit2 in zip(list1, list2):
            sum = digit1 + digit2
            digit = sum%10 + carry
            carry = sum//10
            res.insert(0,digit)
        if carry != 0:
            res.insert(0,carry)
        for i in range(len(res)):
            resL.val = res[i]
            resL = resL.next
        return resL



