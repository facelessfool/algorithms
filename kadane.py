#kadane's algorithm

#used in finding maximum sub array 

 def maxSubArray(self, nums: List[int]) -> int:
        max_so_far= nums[0]
        max_ending_here=0
        n=len(nums)
        
        for i in range(0,n):
            max_ending_here+=nums[i]
            
            if(max_so_far<max_ending_here):
                max_so_far=max_ending_here
            if(max_ending_here<0):
                max_ending_here=0
        return max_so_far