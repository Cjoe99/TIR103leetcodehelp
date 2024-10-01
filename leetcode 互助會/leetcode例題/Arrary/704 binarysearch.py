class solution(object):
    def search(self,nums,target):
        left,right = 0,len(nums)-1
        while right>=left:
            middle = (left + right)//2
            if nums[middle]>target:
                right = middle-1
            elif nums[middle]<target:
                left = middle+1
            else:
                return middle
        return -1