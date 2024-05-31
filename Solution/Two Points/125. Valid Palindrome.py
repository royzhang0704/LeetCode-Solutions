class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True  # 空字串本身就是一個迴文
        start_index = 0
        end_index = len(s) - 1
        while start_index < end_index:  # 整個字串還沒掃完
            # 遇到字元為非數字或英文一律跳過
            while start_index < end_index and not s[start_index].isalnum():
                start_index += 1
            while start_index < end_index and not s[end_index].isalnum():
                end_index -= 1

            # 不管大小寫 所以都當lowercase去check
            if s[start_index].lower() != s[end_index].lower():  # 遇到不同直接Return False 後面不需在判斷
                return False

            # 上方if 沒執行代表目前成功 去找下一對檢查
            start_index += 1
            end_index -= 1
        # 當start_index>=end_index 整個字串跑完 沒被執行False 則返回True
        return True

                
            
          
            
        
