from ingredient import Ingredient

class Recipe():
    def __init__(self, name, ingredients=[]):
        self.name = name
        self.ingredients = ingredients or []

    def add_ingredient(self, ingredient, amount, unit):
        new_ingredient = Ingredient(ingredient, amount, unit)
        self.ingredients.append(new_ingredient)

    def get_ingredients(self):
        return self.ingredients

    @classmethod
    def from_dict(cls, name, ingredients_list):
        recipe = cls(name)
        for ingredient in ingredients_list:
            recipe.add_ingredient(ingredient['name'], ingredient['quantity'], ingredient['unit'])
        return recipe