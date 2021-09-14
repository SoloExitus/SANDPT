def multiply_numbers(*input):
    mult = None
    if not input:
        return mult

    if not type(input) == str:
        input = str(input)

    for c in input:
        if c.isdigit():
            if not mult:
                mult = int(c)
            else:
                mult *= int(c)

    return mult