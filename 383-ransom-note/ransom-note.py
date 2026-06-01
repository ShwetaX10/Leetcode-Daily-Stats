class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        c={}
        for ch in magazine:
            if ch in c:
                c[ch]+=1 
            else:
                c[ch]=1 
        for ch in ransomNote:
            if ch in c and c[ch]>0:
                c[ch]-=1 
            else:
                return False
        return True 
