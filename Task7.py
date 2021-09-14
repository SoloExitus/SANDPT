def combine_anagrams(words: list[str]) -> list:
    lib = dict()

    for word in words:
        lower = word.lower()
        sort = str(sorted(lower))

        if sort in lib:
            lib[sort].append(word)
        else:
            lib[sort] = [word]

    res = []

    for value in lib.values():
        res.append(value)

    return res

print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar", "creams", "scream"]))
# => [ ["cars", "racs", "scar"], ["four"], ["for"], ["potatoes"], ["creams", "scream"] ]