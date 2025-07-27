from recipe import Recipe
from ingredient import Ingredient

def main_menu():
    while True:
        print("\n--- Recipe Assistant ---")
        print("1. Add Recipe")
        print("2. Select Recipes for Shopping List")
        print("3. View Shopping List")
        print("4. Exit")

        choice = input("Enter your choice [1-4]: ").strip()

        if choice == "1":
            add_recipe()
        elif choice == "2":
            select_recipes()
        elif choice == "3":
            view_shopping_list()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def add_recipe():
    print("Adding new recipe...")
    print("Please add the recipe name")
    name = input("Recipe Name: ").strip()
    ingredients = []
    while True:
        print(f"Adding recipe for {name}...")    
        print("Now add the ingredients for the recipe.")
        print("1. New ingredient")
        print("2. Show all ingredients")
        print("3. Finish adding ingredients")
        print("4. Cancel adding recipe")
        choice = input("Enter your choice [1-4]: ").strip()
    
        if choice == "1":
            add_ingredient()
        elif choice == "2":
            print("Current ingredients:")
            for ing in ingredients:
                print(f"- {ing.name}: {ing.quantity} {ing.unit}")
        elif choice == "3":
            if len(ingredients) == 0:
                print("No ingredients added. Please add at least one ingredient.")
            else:
                recipe = Recipe(name, ingredients)
                all_recipes[name] = recipe
                print(f"Recipe '{name}' added successfully!")
                break
        elif choice == "4":
            print("Cancelled adding recipe.")
            break
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def add_ingredient():
    print("Adding new ingredient...")
    name = input("Ingredient Name: ").strip()
    quantity = input("Quantity: ").strip()
    unit = input("Unit (e.g., grams, cups): ").strip()
    
    if name and quantity and unit:
        ingredient = Ingredient(name, quantity, unit)
        ingredients.append(ingredient)
        print(f"Ingredient '{name}' added successfully!")
    else:
        print("Invalid ingredient details. Please try again.")



def select_recipes():
    print("Select recipes for your shopping list:")
    if not all_recipes:
        print("No recipes available. Please add a recipe first.")
        return

    for i, recipe in enumerate(all_recipes.values(), start=1): 
        print(f"{i}. {recipe.name}")
        print("0. Go back to main menu")
    choice = input("Enter the number of the recipe to add to your shopping list (or 0 to go back): ").strip()
    if choice == "0":
        return
    
