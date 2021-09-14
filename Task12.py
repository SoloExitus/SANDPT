from Task11 import Dessert

class JellyBean(Dessert):
    def __init__(self, calories:int, flavor:str):
        super().__init__("JellyBean", calories)
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value: str):
        self._flavor = value

    def is_delicious(self):
        if self._flavor == "black licorice":
            return False
        return super().is_delicious()


test = JellyBean(220, "white licorice")

print(test.is_delicious())

test.flavor = "black licorice"

print(test.is_delicious())
