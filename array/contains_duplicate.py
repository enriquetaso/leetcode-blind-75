def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    char_set = set()
    for element in nums:
        if element in char_set:
            return True
        char_set.add(element)
    return False