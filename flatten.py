def flatten(input_l, flatten_l): 
    """
    Base case (Temel durum)
    """
    if type(input_l) != type([]):  
        flatten_l.append(input_l)
        return

    """
    recursive case (yinelenen durum)
    """
    for i in input_l:
        if type(input_l) == type([]):
            flatten(i, flatten_l)

    return flatten_l

input_l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
result = []


print(flatten(input_l, result))
