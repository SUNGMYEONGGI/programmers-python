def solution(n, t):
    for i in range(0, t):
        n *= 2
        if i == t+1:
            break
    return n