from re import I
import time


def timer_func(func):
    """Execution time of the function object passed"""

    def wrap_func(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Finished in : {(end - start)*1000000:.1f}ms")
        return result

    return wrap_func


@timer_func
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Brute Force
    for index, num in enumerate(nums):
        for aux in nums[index:]:
            if num + aux == target:
                return [nums.index(num), nums.index(aux)]


@timer_func
def twoSum_hash_table(nums, target):
    hash_table = {}  # {2: 0}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in hash_table:
            return [hash_table[diff], index]
        hash_table[num] = index


if __name__ == "__main__":
    print("===========")
    print("Brute force")
    print("===========")
    # nums = [2,7,11,15]
    nums = [2, 11, 15, 7]
    target = 9
    result = twoSum(nums, target)
    print("===========")
    print("Hash table")
    print("===========")
    result2 = twoSum_hash_table(nums, target)
