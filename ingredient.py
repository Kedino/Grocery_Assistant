

class Ingredient():
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    @classmethod
    def create_ingredient(cls, name, unit):
        name = name.strip().title()
        unit = unit.strip().lower()
        if not name or not unit:
            raise ValueError("Name and unit cannot be empty.")
        return cls(name, unit)