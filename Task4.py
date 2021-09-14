def sort_list(mass:list[int]) -> list[int]:
    if not mass:
        return []

    max = mass[0]
    min = mass[0]

    for x in mass:
        if x > max:
            max = x
        if x < min:
            min = x

    for i in range(len(mass)):
        if mass[i] == min:
            mass[i] = max
        elif mass[i] == max:
            mass[i] = min

    mass.append(min)
    return mass
