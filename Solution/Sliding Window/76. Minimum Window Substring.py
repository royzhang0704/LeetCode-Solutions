class Solution:
    """
    time:O(n)
    space:O(m+n)m為s字串的長度 n為t
    """
    def minWindow(self, s: str, t: str) -> str:
        t_counter=Counter(t)
        current_counter={}
        for i in t:
            if i not in current_counter:
                current_counter[i]=0
        def is_contains(current,target):
            for i in current:
                if current[i]<target[i]:
                    return False
            return True
        
        left=0
        min_length=float('inf')
        ans=""
        for right in range(len(s)):
            if s[right] in t:
                current_counter[s[right]]+=1
            while is_contains(current_counter,t_counter):
                if min_length>right-left+1:
                    min_length=right-left+1
                    ans=s[left:right+1]
                if s[left] in current_counter:
                    current_counter[s[left]]-=1
                left+=1
        return "" if len(s)<len(t) else ans
