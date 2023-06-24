from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 2
def test_dish():
    dish_1 = Dish("Pizza", 35.90)
    dish_2 = Dish("Lasanha", 36.90)
    dish_hash = "Dish('Pizza', R$35.90)"
    dish_hash_2 = "Dish('Lasanha, R$36.90)"
    ingredient = Ingredient("farinha")

    assert dish_1.name == "Pizza"

    assert hash(dish_1) == hash(dish_hash)
    assert hash(dish_1) != hash(dish_hash_2)

    assert dish_1 == dish_1
    assert dish_1 != dish_2

    assert repr(dish_1) == dish_hash

    with pytest.raises(TypeError):
        Dish("Pizza", "35.90")

    with pytest.raises(ValueError):
        Dish("Pizza", -36.00)

    assert dish_1.recipe.get("farinha") is None

    dish_1.add_ingredient_dependency(ingredient, 15)

    assert dish_1.get_restrictions() == {Restriction.GLUTEN}
    assert dish_1.get_ingredients() == {ingredient}
