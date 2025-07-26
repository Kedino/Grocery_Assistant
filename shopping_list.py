from recipe import Recipe

class ShoppingList():
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def get_all_ingredients(self):
        all_ingredients = []
        for recipe in self.recipes:
            all_ingredients.extend(recipe.get_ingredients())
        return all_ingredients

    def clear_list(self):
        self.recipes = []

