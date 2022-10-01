# Sum of 2 numbers in list equal target
def twoSum(nums, target: int):
        for i in range(len(nums)):
            copy_nums = nums.copy()
            del copy_nums[i]
            if target - nums[i] in copy_nums:
                return [i, copy_nums.index(target - nums[i])+1]

# Sum of 2 sub arrays are equal
def findSubarrays(nums) -> bool:
        def target_exist(num_list, target):
            for i in range(len(num_list)-1):
                if num_list[i] + num_list[i + 1] == target:
                    return True
            return False
        
        for i in range(len(nums) - 1):
            if target_exist(nums[i+1:], nums[i] + nums[i+1]):
                return True
        return False


if __name__=='__main__':
    nums = [80,42,75,45,45,73,17,31,30,98,20,32,66,90,21,85,83,24,87,81,77,10,48,25,44,76,23,13,22,9,88,31,29,64,68,38,44,59,40,12,97,33,34,32,93,26,89,64,55,76,77,66,74,52,34,100,18,5,20,45,7,75,70,86,1,30,20,63,99,13,66,42,2,17,80,43,11,52,16,71,73,30,38,76,21,81,27,76,59,62,72,21,51,5,79,20,93,91,33,13]
    print(findSubarrays(nums))