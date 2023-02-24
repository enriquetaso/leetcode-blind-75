# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if
# the input string is valid.

# An input string is valid if:
# - Open brackets must be closed by the same type of brackets.
# - Open brackets must be closed in the correct order.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false


def isValid(s: str) -> bool:
    """
    :type s: str
    :returns: bool
    """
    stack = []
    hash_simbols = {"}": "{", ")": "(", "]": "["}
    for simbol in s:
        if stack and simbol in hash_simbols:
            if stack[-1] == hash_simbols[simbol]:
                stack.pop()
            else:
                return False
        else:
            stack.append(simbol)

    return True if not stack else False
