class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        '''if n==1:
            return True 
        else:
            for i in range(2,n+1):
                if n%i==0:
                    if i==2 or i==3 or i==5:
                        c+=1 
            if c==3 or c==2 or c==1:
                return True 
            else:
                return False'''
        if n==1 :
            return True 
        elif n<=0:
            return False
        else:
            for i in [2,3,5]:
                while n%i==0:
                    n//=i 
            return n==1

        