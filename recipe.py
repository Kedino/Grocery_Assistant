from ingredient import Ingredient

class Recipe():
    def __init__(self, name, ingredients=[]):
        self.name = name
        self.ingredients = ingredients or []

    def add_ingredient(self, usage):
        self.ingredients.append(usage)

    def get_ingredients(self):
        return self.ingredients

    @classmethod
    def from_dict(cls, name, ingredients_list):
        recipe = cls(name)
        for ing in ingredients_list:
            ingredient_obj = Ingredient(ing['name'], ing['unit'])
            usage = IngredientUsage(ingredient_obj, ing['quantity'])
            recipe.add_ingredient(usage)
        return recipe
    

class IngredientUsage():
    def __init__(self, ingredient, quantity):
        self.ingredient = ingredient
        self.quantity = quantity

    @property
    def name(self):
        return self.ingredient.name

    @property
    def unit(self):
        return self.ingredient.unit
    
    def as_dict(self):
        return {
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit
        }