import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        if not source_path:
            raise ValueError("Passe o caminho do arquivo")
        self.dishes = set()
        self.ingredients = set()
        self.read_file(source_path)

    def read_file(self, source_path: str) -> None:
        with open(source_path, "r") as file:
            recipes = csv.reader(file)
            next(recipes)

            for line in recipes:
                name, price, ingredient_name, quantity = line[:4]
                if float(price) < 0 or int(quantity) < 0:
                    raise ValueError(
                        "Preço ou quantidade deve ser maior que 0"
                    )

                ingredient = next(
                    (
                        ing
                        for ing in self.ingredients
                        if ing.name == ingredient_name
                    ),
                    None,
                )
                if ingredient is None:
                    ingredient = Ingredient(ingredient_name)
                    self.ingredients.add(ingredient)

                dish = next((d for d in self.dishes if d.name == name), None)
                if dish is None:
                    dish = Dish(name, float(price))
                    self.dishes.add(dish)

                dish.add_ingredient_dependency(ingredient, int(quantity))
