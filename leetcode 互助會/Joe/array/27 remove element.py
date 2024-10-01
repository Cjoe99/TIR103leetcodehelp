# class Solution:  #要知道数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖。
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while check_num <len(nums):
#             check_num  = 0
#             pass_num = 0
#             if nums[check_num] != val :
#                 nums[pass_num] = nums[check_num]
#                 pass_num += 1
#             check_num += 1
#         return pass_num
# #以上跑不動，仔細看一下，while 後面的判斷式沒有先定義，所以要先把定義放前面

class Solution:  #要知道数组的元素在内存地址中是连续的，不能单独删除数组中的某个元素，只能覆盖。
    def removeElement(self, nums: List[int], val: int) -> int:
        check_num  = 0
        pass_num = 0
        size = len(nums)
        while check_num < size :
            if nums[check_num] != val :
                nums[pass_num] = nums[check_num]
                pass_num += 1
            check_num += 1
        return pass_num