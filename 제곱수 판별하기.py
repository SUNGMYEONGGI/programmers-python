import math

def solution(n):
    sq_num = math.sqrt(n)
    if math.pow(int(sq_num), 2) == n:
        return 1
    else:
        return 2