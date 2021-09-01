class Solution(object):
    
    #Time (nlog(n)) | Space O(n)
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        countSmaller = []
        ret = nums[:]
        
        for i in reversed(range(len(nums))):
            value = nums[i]
            
            # Time O(logn)
            pos = find_index(countSmaller, value)
            
            # Time O(n)
            # countSmaller.insert(pos, value)
            # memmove
            countSmaller[pos:pos] = [ value ]
            
            ret[i] = pos
            
        return ret
    
# Time O(log(n))    
def find_index(arr, v):
    lo = 0
    hi = len(arr)
    
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < v:
            lo = mid + 1
        else:
            hi = mid
            
    return lo