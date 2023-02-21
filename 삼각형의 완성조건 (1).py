def solution(sides):
    sides = sorted(sides)
    
    if sides[2] < sides[0] + sides[1]:
        return 1
    elif sides[2] == sides[0] + sides[1]:
        return 2
    else:
        return 2