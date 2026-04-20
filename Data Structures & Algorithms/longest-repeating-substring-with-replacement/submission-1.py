class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxfre=0
        count={}
        maxlen=0
        l=0
        for r in range (len(s)):
            count[s[r]]=1+count.get(s[r],0)
            maxfre=max(maxfre,count[s[r]])


            while (r-l+1)- maxfre >k:
                count[s[l]]-=1
                l+=1
            
            maxlen=max(maxlen,r-l+1)

        return maxlen
