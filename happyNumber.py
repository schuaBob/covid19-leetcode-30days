class Solution:
    def isHappy(self,n:int)->bool:
        while n>6:
            happyList = list(map(int,list(str(n))))
            for i,v in enumerate(happyList):
                if i==0:
                    n=0
                n +=v*v
        return True if n==1 else False