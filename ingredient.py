

class Ingredient():
    def __init__(self, name, unit):
        self.name = name.strip().title()
        self.unit = unit.strip().lower()

    @classmethod
    def create_ingredient(cls, name, unit):
        name = name.strip().title()
        unit = unit.strip().lower()
        if not name or not unit:
            raise ValueError("Name and unit cannot be empty.")
        return cls(name, unit)
    
    def _normalize(self, word):
        word = word.strip().lower()
        if word.endswith("s") and len(word) > 1:
           word = word[:-1]
        return word
    
    def __eq__(self, other):
        return (
            isinstance(other, Ingredient)
            and self._normalize(self.name) == self._normalize(other.name)
            and self._normalize(self.unit) == self._normalize(other.unit)
        )

    def __hash__(self):
        return hash((self._normalize(self.name), self._normalize(self.unit)))