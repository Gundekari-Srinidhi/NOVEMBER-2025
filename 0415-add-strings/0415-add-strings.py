class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1=0
        for i in num1:
            n1=n1*10+int(i)
        n2=0
        for i in num2:
            n2=n2*10+int(i)
        n=n1+n2
        if n==0:
            return "0"
        s=""
        while n!=0:
            rem=n%10
            s+=str(rem)
            n=n//10
        return s[::-1]
        