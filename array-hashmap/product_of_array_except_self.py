# Given an integer array nums, return an array answer
# such that answer[i] is equal to the product of all
# the elements of nums except nums[i].

# The product of any prefix or suffix of nums is
# guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time
# and without using the division operation.

from math import prod
from typing import List


def productExceptSelf_wrong(nums: List[int]) -> List[int]:
    """Time Limit Exceeded

    Time complexity:  O(n^2)
    """
    result = []
    for i in range(len(nums)):
        r = 1
        prefix = nums[:i]
        suffix = nums[(i + 1) :]
        for item in prefix + suffix:
            r *= item
        result.append(r)
    return result


def productExceptSelf(nums: List[int]) -> List[int]:
    """Given an integer array nums, return an array

    answer such that answer[i] is equal to the product
    of all the elements of nums except nums[i].

    Time complexity: O(n)
    Memory: O(1)
    """
    # this doesnt count as extra memory
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
    return res


def productExceptSelf_try(nums):
    """Time Limit Exceeded

    Time complexity:  O(n)
    Memory: O(n)
    """

    #           [1,  2,   3,   4]
    # prefix =  [1,  2,   6,  24]
    # postfix = [24, 24,  12,  4]

    result = [1] * len(nums)
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)

    for i in range(len(nums)):
        if i == 0:
            prefix[0] = nums[0]
        else:
            prefix[i] = prefix[i - 1] * nums[i]

    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            postfix[i] = nums[i]
        else:
            postfix[i] = postfix[i + 1] * nums[i]

    for i in range(len(nums)):
        if i == 0:
            result[i] = postfix[i + 1]
        elif i == len(nums) - 1:
            result[i] = prefix[i - 1]
        else:
            result[i] = prefix[i - 1] * postfix[i + 1]

    print("nums", nums)
    print("prefix", prefix)
    print("posfix", postfix)
    return result


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    result = productExceptSelf_try(nums1)
    print(result)

    # nums2 = [-1, 1, 0, -3, 3]
    # result2 = productExceptSelf(nums2)
    # print(result2)

    # nums3 = [1, 2, 3, 4, 5]
    # result3 = productExceptSelf(nums3)
    # print(result3)

    # nums4 = [1, 2, 3, 4, 5, 6]
    # result4 = productExceptSelf(nums4)
    # print(result4)

    # nums5 = [1, 2, 3, 4, 5, 6, 7]
    # result5 = productExceptSelf(nums5)
    # print(result5)

    # nums6 = [1, 2, 3, 4, 5, 6, 7, 8]
    # result6 = productExceptSelf(nums6)
    # print(result6)

    # nums7 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # result7 = productExceptSelf(nums7)
    # print(result7)

    # nums8 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # result8 = productExceptSelf(nums8)
    # print(result8)

    # nums9 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # result9 = productExceptSelf(nums9)
    # print(result9)

    # nums10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # result10 = productExceptSelf(nums10)
    # print(result10)

    # nums11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # result11 = productExceptSelf(nums11)
    # print(result11)
