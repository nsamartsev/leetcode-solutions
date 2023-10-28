from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map = dict()
        brackets_map[')'] = "("
        brackets_map[']'] = "["
        brackets_map['}'] = "{"
        
        is_valid = False
        stack = deque()
        
        for i in range(len(s)):
            single_char = s[i]
            
            if single_char in brackets_map.values():
                stack.append(single_char)
            elif single_char in brackets_map.keys():
                if len(stack) == 0 or stack.pop() != brackets_map[single_char]: 
                    return False
                
        if len(stack) == 0:
            is_valid = True
        
        return is_valid
        

assert Solution().isValid("()") == True