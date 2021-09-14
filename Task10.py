import re

def count_words(string: str) -> dict[str, int]:
    clear = re.sub(r'[^\w\s]', '', string)
    clear = clear.lower()
    words = clear.split()

    res = dict[str, int]()

    for word in words:
        if (word in res):
            res[word] = res[word] + 1
        else:
            res[word] = 1
    return res


print(count_words("A man, a plan, a canal -- Panama")) # => {"a" => 3, "man" => 1,"canal" => 1, "panama" => 1, "plan" => 1}
print(count_words("Doo bee doo bee doo")) # => {"doo" => 3, "bee" =>2}