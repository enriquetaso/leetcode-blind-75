# Check if all elements of one array is in another array
# I have these two arrays:
# A = [1,2,3,4,5,6,7,8,9,0]
# And
# B = [4,5,6,7]
# Is there a way to check if B is a sublist in A with the same exact order of items?


def find_sublist(list1, list2):
    """Find sublist in list1 with the same order of items."""
    # O(n) solution
    if list2[0] in list1:
        index = list1.index(list2[0])
        return all(list1[index + i] == list2[i] for i in range(len(list2)))
    return False


def check_all_elements_unordered(list1, list2):
    # wrong, this solution does not imply the order of the elements!
    # return set(list2).issubset(set(list1))
    return all(x in list1 for x in list2)


if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list2 = [4, 5, 6, 7]
    list3 = [4, 5, 6, 7, 8]
    list4 = [4, 5, 6, 7, 8, 9, 0]
    print(find_sublist(list1, list2))
