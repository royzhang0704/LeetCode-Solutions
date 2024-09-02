class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result=[]
        num=1
        for i in target:
            while num<i:
                result.extend(["Push","Pop"])
                num+=1
            result.append("Push") #當前value 
            num+=1
        return result
