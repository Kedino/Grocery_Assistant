from recipe import Recipe, IngredientUsage
from ingredient import Ingredient
from shopping_list import ShoppingList
from recipe_list import RECIPE_MAP

class GroceryAssistant():
    def __init__(self):
        self.all_recipes = {}
        self.shopping_list = ShoppingList()
        self.all_ingredients = []
        for name, ing_list in RECIPE_MAP.items():
            self.all_recipes[name] = Recipe.from_dict(name, ing_list)
        for recipe in self.all_recipes.values():
            for usage in recipe.get_ingredients():
                ingredient = Ingredient(usage.name, usage.unit)
                if ingredient not in self.all_ingredients:
                    self.all_ingredients.append(ingredient)

    def main_menu(self):
        while True:
            print("\n--- Recipe Assistant ---")
            print("1. Create New Recipe")
            print("2. Select Recipes for Shopping List")
            print("3. View Shopping List")
            print("4. Exit")

            choice = input("Enter your choice [1-4]: ").strip()

            if choice == "1":
                self.add_recipe()
            elif choice == "2":
                self.select_recipes()
            elif choice == "3":
                self.view_shopping_list()
            elif choice == "4":
                print("Goodbye!")
                break
            else:
                print("Invalid input. Please enter a number from 1 to 4.")

    def add_recipe(self):
        print("Creating new recipe...")
        print("Please add the recipe name")
        name = input("Recipe Name: ").strip()
        usages = []
        while True:
            print(f"Adding recipe for {name}...")    
            print("Now add the ingredients for the recipe.")
            print("1. Add ingredient")
            print("2. Show all ingredients")
            print("3. Finish adding ingredients")
            print("4. Cancel adding recipe")
            choice = input("Enter your choice [1-4]: ").strip()
        
            if choice == "1":
                self.add_ingredient(usages)
            elif choice == "2":
                print("Current ingredients:")
                for ing in usages:
                    print(f"- {ing.name.title()}: {ing.quantity} {ing.unit}")
            elif choice == "3":
                if len(usages) == 0:
                    print("No ingredients added. Please add at least one ingredient.")
                else:
                    recipe = Recipe(name, usages)
                    self.all_recipes[name] = recipe
                    print(f"Recipe '{name}' added successfully!")
                    break
            elif choice == "4":
                print("Cancelled adding recipe.")
                break
            else:
                print("Invalid input. Please enter a number from 1 to 4.")

    
    def add_ingredient(self, usages):
        matches = []
        while True:
            if matches:
                print("Matching ingredients:")
                for i, ing in enumerate(matches, start=1):
                    print(f"{i}. {ing.name.title()} ({ing.unit})")
                print("Select an ingredient by number, or search again (or 0 to create new): ")
            else:
                print("Enter ingredient name to search (or 0 to create new): ")
            choice = input("> ").strip()
            if choice == "0":
                return self.create_new_ingredient(usages)
            if matches and choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(matches):
                    ingredient = matches[choice - 1]
                    quantity = self.prompt_for_quantity()
                    usage = IngredientUsage(ingredient, quantity)
                    usages.append(usage)
                    print(f"Added {quantity} {ingredient.unit} of {ingredient.name.title()} to the recipe.")
                    return
                else:
                    print("Invalid choice. Please select a valid ingredient number, search again, or select 0 to create new ingredient.")
            elif choice == "":
                print("Search term cannot be empty. Please try again.")
            else:
                matches = self.find_ingredient(choice)
                if not matches:
                    print("No matching ingredients found.")
    





    def find_ingredient(self, search_term):
        search_term = search_term.lower()
        matches = []
        for ing in self.all_ingredients:
            if search_term in ing.name.lower():
                matches.append(ing)
        return matches

    def create_new_ingredient(self, usages):
        name = input("Enter new ingredient name: ").strip()
        unit = input("Enter unit (e.g., grams, cups): ").strip()
        ingredient = Ingredient.create_ingredient(name, unit)
        if ingredient not in self.all_ingredients:
            self.all_ingredients.append(ingredient)
        quantity = self.prompt_for_quantity()
        usage = IngredientUsage(ingredient, quantity)
        usages.append(usage)
        print(f"Added {quantity} {ingredient.unit} of {ingredient.name.title()} to the recipe.")        

    def prompt_for_quantity(self):
        while True:
            quantity_input = input("Enter quantity: ").strip()
            try:
                quantity = float(quantity_input)
                return quantity
            except ValueError:
                print("Please enter a valid number for quantity.")


    def select_recipes(self):
        print("Select recipes for your shopping list:")
        if not self.all_recipes:
            print("No recipes available. Please add a recipe first.")
            return
        while True:
            print("\nAvailable Recipes:")
            for i, recipe in enumerate(self.all_recipes.values(), start=1): 
                print(f"{i}. {recipe.name}")
                print("0. Go back to main menu")
            choice = input("Enter the number of the recipe to add to your shopping list (or 0 to go back): ").strip()
            if choice == "0":
                return
            if not choice.isdigit():
                print("Invalid choice. Please enter a number.")
                continue
            choice = int(choice)            
            if 1 <= choice <= len(self.all_recipes):
                recipe_name = list(self.all_recipes.keys())[choice - 1]
                recipe = self.all_recipes[recipe_name]
                self.shopping_list.add_recipe(recipe)
                print(f"Recipe '{recipe_name}' added to shopping list.")
            else:
                print("Invalid choice. Please select a valid recipe number.")


    def view_shopping_list(self):
        if len(self.shopping_list.recipes) == 0:
            print("Your shopping list is empty.")
            return
        print("\nYour Shopping List for recipes:")
        for recipe in self.shopping_list.recipes:
            print(f"- {recipe.name}")
        print("\nCombined ingredients for all recipes:")
        combined_ingredients, unit_mismatches = self.shopping_list.get_combined_ingredients()
        for ingredient in combined_ingredients.values():
            print(f"- {ingredient.name.title()}: {ingredient.quantity} {ingredient.unit}")
        if unit_mismatches:
            print("\nNotice: Unit mismatches found:")
            for name, mismatches in unit_mismatches.items():
                print(f"{name.title()} was present in different units:")
                for quantity, unit in mismatches:
                    print(f"  - {quantity} {unit}")


            
