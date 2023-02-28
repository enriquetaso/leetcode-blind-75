def jumpingOnClouds(c):
    safe_jump = {0: True, 1: False}
    jumps = position = 0
    while position != (len(c) - 1):
        if position + 2 < len(c) and safe_jump[c[position + 2]]:
            position += 2
            jumps += 1
        else:
            position += 1
            jumps += 1
    return jumps


def jumpingOnClouds_recursive(c):
    if len(c) == 1:
        return 0
    if len(c) == 2:
        return 0 if c[1] == 1 else 1
    if c[2] == 1:
        return 1 + jumpingOnClouds_recursive(c[1:])
    if c[2] == 0:
        return 1 + jumpingOnClouds_recursive(c[1:])


if __name__ == "__main__":

    case1_clouds = [0, 1, 0, 0, 0, 1, 0]
    print(jumpingOnClouds(case1_clouds))
    print("The result should be 3")

    clouds = [0, 0, 1, 0, 0, 1, 0]
    print(jumpingOnClouds(clouds))
    print("The result should be 4")

    case3 = [0, 0, 0, 1, 0, 0]
    print(jumpingOnClouds(case3))
