from cookbook import RECIPE_MAP
from recipe import Recipe
from shopping_list import ShoppingList
from menu import main_menu

all_recipes = {}
for name, ing_list in RECIPE_MAP.items():
    all_recipes[name] = Recipe.from_dict(name, ing_list)

shopping_list = ShoppingList()




def main():
    print("Hello from groceryassistant!")


if __name__ == "__main__":
    main()
