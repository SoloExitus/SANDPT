
class Dessert:
    def __init__(self, name:str, calories:int):
        self._name = name
        self._calories = calories

    @property
    def name(self):
        return self._name

    @property
    def calories(self):
        return self._calories

    @name.setter
    def name(self, value:str):
        self._name = value

    @calories.setter
    def calories(self, value:int):
        self._calories = value

    def is_healthy(self) -> bool:
        if self._calories < 200:
            return True
        return False

    def is_delicious(self):
        return isinstance(self, Dessert)

# test = Dessert('cake', 320)
#
# print(test.name, test.calories, test.is_healthy(), test.is_delicious())
# test.name = 'pie'
# print(test.name, test.calories, test.is_healthy(), test.is_delicious())
# test.calories = 199
# print(test.name, test.calories, test.is_healthy(), test.is_delicious())