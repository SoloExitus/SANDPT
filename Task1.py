import re

def is_palindrome(input: str) -> bool:
    if not type(input) == str:
        return False

    clearStr = re.sub(r'[^\w]', '', input)
    #ignor = '''!()-[]{};?@#$%:'"\,./^&*_ '''

    clearStr = clearStr.lower()
    reverseStr="".join(reversed(clearStr))
    if (clearStr == reverseStr):
        return True
    return False