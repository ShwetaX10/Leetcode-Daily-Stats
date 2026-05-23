import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''c=0 
        if n==0 or n==1:
            return 0 
        else:
            for i in range(2,n):
                a=self.countp(i)
                c=c+a
                
            return c
    def countp(self,num):
        count=0
        flag=True
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i==0:
                flag=False
                break
        if flag==True:
            count=1 
            return count 
        else:
            count=0 
            return count'''
        
        if n < 2:
            return 0
        
        # 1. Initialize all as prime
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        # 2. Mark non-primes
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Start from i*i because smaller multiples handled by earlier primes
                for j in range(i*i, n, i):
                    is_prime[j] = False
        
        # 3. Count remaining primes
        return sum(is_prime)
        
        


       
            

        