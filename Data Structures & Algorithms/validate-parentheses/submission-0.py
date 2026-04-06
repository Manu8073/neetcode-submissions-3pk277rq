class Solution:
    def isValid(self, s: str) -> bool:
        mapc={')':'(',']':'[','}':'{'}
        stack=[]
        for ch in s:
            if ch in mapc:
                if not stack or stack.pop()!=mapc[ch]:
                    return False
            else :
                stack.append(ch)
        return not stack
