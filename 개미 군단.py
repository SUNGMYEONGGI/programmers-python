# 개미군단 - 내 풀이
def solution(hp):
    
    if hp % 5 == 0:
        return hp // 5
    elif hp % 5 == 1 or hp % 5 == 3:
        return (hp // 5) + 1
    else:
        return (hp // 5) + 2


# 개미군단 - 다른 사람 풀이(1)
def solution(hp):    
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)


# 개미군단 - 다른 사람 풀이(2)
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer