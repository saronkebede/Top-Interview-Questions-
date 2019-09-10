class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        curr = l1
        curr2 = l2
        str1=""
        str2=""
        while(curr != None):
            str1+=str(curr.val)
            curr = curr.next
        str1 = str1[::-1]
        while(curr2 != None):
            str2+=str(curr2.val)
            curr2 = curr2.next
        str2 = str2[::-1]
        
        print("String1:  "+ str1)
        print("String2:  "+ str2)
    
        value1 = int(str1)
        value2 = int(str2)
    
        total = value1 + value2
        total = str(total)
        print("Total:  "+total)
    
        l3 = ListNode(int(total[len(total)-1]))
        curr = l3
        for i in range(len(total)-2,-1,-1):
            value = int(total[i])
            node = ListNode(value)
            curr.next = node 
            curr = curr.next
        
        return l3
