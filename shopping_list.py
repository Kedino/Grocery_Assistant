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
    
    def get_combined_ingredients(self):
        combined_ingredients = {}
        unit_mismatches = {}
        for recipe in self.recipes:
            for ingredient in recipe.get_ingredients():
                key = ingredient.name.lower()
                if key in combined_ingredients:
                    if combined_ingredients[key].unit == ingredient.unit:
                        combined_ingredients[key].quantity += ingredient.quantity
                    else:
                        if key not in unit_mismatches:
                            unit_mismatches[key] = [
                                (combined_ingredients[key].quantity, combined_ingredients[key].unit)
                            ]
                        mismatch_pair = (ingredient.quantity, ingredient.unit)
                        if mismatch_pair not in unit_mismatches[key]:
                            unit_mismatches[key].append(mismatch_pair)
                else:
                    combined_ingredients[key] = ingredient
        return combined_ingredients, unit_mismatches

    def clear_list(self):
        self.recipes = []

