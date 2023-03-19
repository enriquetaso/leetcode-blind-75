def maximum_subarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    cur_sum = 0
    for n in nums:
        cur_sum = max(0, cur_sum + n)
        max_sum = max(max_sum, cur_sum)
    return max_sum


def maximum_subarray2(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_sum = nums[0]
    cur_sum = 0
    for n in nums:
        if cur_sum < 0:
            cur_sum = n
        cur_sum += n
        max_sum = max(max_sum, cur_sum)
    return max_sum


def maximum_subarray_dp(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        print("i:", i, "dp[i]:", dp[i], "dp[i - 1]:", dp[i - 1], "nums[i]:", nums[i])
        dp[i] = max(nums[i], dp[i - 1] + nums[i])
    print("dp:", dp)
    return max(dp)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maximum_subarray(nums)
    if result == 6:
        print("Right!")
    else:
        print("Wrong!")
