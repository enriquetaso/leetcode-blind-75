from typing import List


def longestConsecutive_using_sort_and_set(nums: List[int]) -> int:
    """

    Time complexity: O(nlogn)
    Space complexity: O(n)
    """
    nums.sort()
    secuence = 0
    secuence_list = set()

    for i, n in enumerate(nums):     
        if n == nums[-1]:
            break
        if nums[i+1] == n+1 or nums[i+1] == n:
            secuence_list.add(n)
            secuence_list.add(nums[i+1])
        else:
            secuence_list.clear()
        secuence = max(secuence, len(secuence_list))
    return secuence


def longestConsecutive(nums: List[int]) -> int:
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    numSet = set(nums)
    longest = 0

    for n in nums:
        # check that it is the start of the secuence
        if (n-1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length +=1
            longest = max(longest, length)
    return longest


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))
    print(longestConsecutive_using_sort_and_set(nums))
    # nums2 = [1,3,5,7]
    # print(longestConsecutive(nums2))
    nums3 = [1,2,0,1]
    print(longestConsecutive(nums3))
    print(longestConsecutive_using_sort_and_set(nums3))
    # nums4 = [0,3,7,2,5,8,4,6,0,1]
    # print(longestConsecutive(nums4))
    
    
