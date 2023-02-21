# A phrase is a palindrome if, after converting all uppercase
# letters into lowercase letters and removing all
# non-alphanumeric characters, it reads the same forward and
# backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false
# otherwise.


def isPalindrome_two_pointers(s: str) -> bool:
    """
    :type s: str
    :rtype: bool
    Linear time algorith O(n) because we still need to iterate throw the entire string
    but memory usage/ complexity is O(1) because we are not using any extra memory.
    """
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not alphNum(s[l]):
            l += 1
        while r > l and not alphNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True


def alphNum(c: str) -> bool:
    """Manually check alf num."""
    return (
        ord("A") <= ord(c) <= ord("Z")
        or ord("a") <= ord(c) <= ord("z")
        or ord("0") <= ord(c) <= ord("9")
    )


def isPalindrome_memory_usage(s: str) -> bool:
    """Memory usage because of new string."""
    formatted_string = "".join(char for char in s.lower() if char.isalnum())
    return formatted_string == formatted_string[::-1]
