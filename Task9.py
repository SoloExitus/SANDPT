def connect_dicts(firstDict: dict, secondDict: dict) -> dict:
    firstSum = sum(firstDict.values())
    secondSum = sum(secondDict.values())

    union = None

    if (firstSum > secondSum):
        #union = {**secondDict, **firstDict} # for python < 3.9
        union = secondDict | firstDict # for python >= 3.9
    else:
        #union = {**firstDict, **secondDict} # for python < 3.9
        union = firstDict | secondDict  # for python >= 3.9

    res = sorted(filter(lambda x: x[1] >= 10, union.items()), key=lambda x: x[0], reverse=True)
    return dict(res)

print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 })) # => { "c": 11, "b": 12 }
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 })) # => { d: 11, "c": 12, "a": 13 }
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # => { "c": 11, "b": 12, "a": 15 }


