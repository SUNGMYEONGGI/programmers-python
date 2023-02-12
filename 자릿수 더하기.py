def solution(n):
    answer = 0
    num_n = list(map(int, str(n)))
    
    for i in num_n:
        answer += i
    return answer