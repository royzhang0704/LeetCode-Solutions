class Solution:

    def encode(self, strs: List[str]) -> str:
        result=""
        for i in strs:
            result+=str(len(i))+"/"+i
        return result
    def decode(self, s: str) -> List[str]:
        result=[]
        i,n=0,len(s)
        while i<n:
            j=i
            while j<n and s[j]!="/":
                j+=1
            length=int(s[i:j])
            result.append(s[j+1:j+length+1])
            i=j+length+1
        return result

"""
    input=>  ["we" ,"say",":","yes"]
            ="2/we3/say/1:/3/yes
    encode=> "wesay:yes"
    decode=> ["we","say",":","yes"]

        2/we3/say/1/:3/yes len=18
         i
             j
    """
