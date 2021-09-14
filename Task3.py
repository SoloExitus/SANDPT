def is_numeric(x):
    if type(x) == int or type(x) == float:
        return True
    return False

def max_odd(array:list):
    max = None
    for x in array:
        if is_numeric(x):
            if x % 2 == 1:
                if not max:
                    max = x
                elif x > max:
                    max = x
    return max
