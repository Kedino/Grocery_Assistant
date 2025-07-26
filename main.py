from cookbook import RECIPE_MAP
from recipe import Recipe

all_recipes = {}
for name, ing_list in RECIPE_MAP.items():
    all_recipes[name] = Recipe.from_dict(name, ing_list)


def main():
    print("Hello from groceryassistant!")


if __name__ == "__main__":
    main()
