class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        curr1, curr2 = list1, list2
        val1, val2 = [], []
        while curr1:
            val1.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            val2.append(curr2.val)
            curr2 = curr2.next

        val1.extend(val2)
        val1.sort()

        head = ListNode(val1[0])
        val1.pop(0)
        dummy = head
        for i in val1:
            newNode = ListNode(i)
            dummy.next  = newNode
            dummy = newNode
        dummy.next = None
        return head

    #Recursion
    class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if list1 == None:
                return list2
            if list2 == None:
                return list1

            if list1.val <= list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2