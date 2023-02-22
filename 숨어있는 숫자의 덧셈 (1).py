def solution(my_string):
    answer = 0
    list_eng = "123456789"
    
    for i in my_string:
        for j in list_eng:
            if i == j:
                answer += int(i)
    return answer