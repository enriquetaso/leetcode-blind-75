# Problem: Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


def containsDuplicateBruteforce(nums):
    """Brute force

    Complexity
    - Time complexity:O(n^2)
    - Space complexity:O(1)
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False


def containsDuplicateSorting(nums):
    """Sorting

    Complexity
    - Time complexity:O(nlogn)
    - Space complexity:O(1)
    """
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


def containsDuplicate(nums):
    """Use set

    Complexity
    - Time complexity:O(n)
    - Space complexity:O(n)
    """
    return len(set(nums)) < len(nums)


def containsDuplicate(nums):
    """Use set without lentgh comparison

    Complexity
    - Time complexity:O(n)
    - Space complexity:O(n)
    """
    char_set = set()
    for element in nums:
        if element in char_set:
            return True
        char_set.add(element)
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(containsDuplicate(nums))
