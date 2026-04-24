class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countt=Counter(t)
        window={}

        res=[-1,-1]
        res_len=float('inf')
        need=len(countt)
        have=0
        left=0

        for right in range(len(s)):

            char =s[right]
            window[char]=window.get(char,0)+1


            if char in countt and window[char]==countt[char]:
                have+=1
            
            while need==have:
                if (right-left)+1 < res_len:
                    res=[left,right]
                    res_len=right-left+1

                window[s[left]]-=1
                if s[left] in countt and window[s[left]]<countt[s[left]]:
                    have-=1
                
                left+=1
        l,r=res
        return s[l:r+1] if res_len!=float('inf') else ""
