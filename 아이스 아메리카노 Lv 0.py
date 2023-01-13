def solution(money):
    coffee = 5500
    answer = []
    
    count = money // coffee
    나머지 = money - (coffee * count)
    
    answer.append(count)
    answer.append(나머지)
    return answer