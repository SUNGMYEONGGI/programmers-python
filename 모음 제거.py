def solution(my_string):
    str_remv = ['a', 'e', 'i', 'o', 'u']
    
    for i in str_remv:
        my_string = my_string.replace(i, '')
    return my_string