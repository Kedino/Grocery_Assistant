import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ingredient import Ingredient
from recipe import Recipe

test_cases = [
    {
        "name": "testing ingredient.py",
        "func": Ingredient,
        "test_args": [
            ("flour", 200, "grams"),
        ],
        "expected": [
            {"name": "flour", "quantity": 200, "unit": "grams"}
        ],
        "check": lambda obj, exp: all(
            getattr(obj, key) == val for key, val in exp.items()
        ),
        "run": False # Set this to True if you want to run these tests
    },
    {
        "name": "testing recipe.py",
        "func": Recipe,
        "test_args": [
            ("Scrambled Eggs", []),
        ],
        "expected": [
            {"name": "Scrambled Eggs", "ingredients": []},
        ],
        "check": lambda obj, exp: obj.name == exp["name"] and obj.ingredients == exp["ingredients"],
        "run": False # Set this to True if you want to run these tests
    },
]

def run_tests():
    for test_group in test_cases:
        if not test_group.get("run", True): 
            print(f"--- Skipping {test_group['name']} ---")
            print()
            continue 
            
        print(f"--- {test_group['name']} ---")

        for i, args in enumerate(test_group["test_args"]):
            obj = test_group["func"](*args)
            exp = test_group["expected"][i]
            passed = test_group["check"](obj, exp)
            if passed:
                print(f"Test passed for args {args}")
            else:
                print(f"Test FAILED for args {args}")
            print()

if __name__ == "__main__":
    run_tests()