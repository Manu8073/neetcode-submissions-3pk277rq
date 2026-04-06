class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxl=0
        total=0
        maxr=0
        while l<r:
            maxl=max(maxl,height[l])
            maxr=max(maxr,height[r])
            if maxl<maxr:
                total+=maxl-height[l]
                l+=1
            else:
                total+=maxr-height[r]
                r-=1
        return total
            