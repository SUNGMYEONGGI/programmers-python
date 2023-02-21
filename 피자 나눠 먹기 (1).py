def solution(n):
    answer = 0
    pizza_piece = 7
    
    if n % 7 == 0:
        return n / 7
    elif n % 7 != 0:
        return (n // 7) +1
    
    return answer