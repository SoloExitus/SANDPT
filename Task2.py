def is_numeric(x):
    if type(x) == int or type(x) == float:
        return True
    return False

def coincidence(*args) -> list:
    res = []
    if len(args) < 2:
        return res

    array = args[0]
    range = args[1]

    min = range[0]
    max = range[len(range) - 1] + 1

    for x in array:
        if (is_numeric(x)):
            if (x >= min and x < max) :
                res.append(x)

    return res
