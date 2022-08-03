class Solution(object):
    def shortestToChar(self, s, c):
        s1=s
        cIndex = []
        rList = [0]*len(s)
        idx=0
        for char in s:
            if char==c:
                cIndex.append(idx)
            idx+=1
        print(cIndex)
        for index, char in enumerate(s):
            # middle = cIndex[len(cIndex)//2]
            if index in cIndex:
                rList[index]=0
            elif index<cIndex[0] or index>cIndex[-1]:
                rList[index]=min(abs(index-cIndex[-1]),abs(index-cIndex[0]))
            else:
                leftIdx = s[:index].rfind(c)
                rightIdx = s[index:].find(c) + index
                rList[index]=min(abs(index-leftIdx),abs(index-rightIdx))
        return rList

    """
        :type s: str
        :type c: str
        :rtype: List[int]
    """