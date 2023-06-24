from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501 # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    assert hash(Ingredient("farinha")) == hash(Ingredient("farinha"))
    assert hash(Ingredient("farinha")) != hash(Ingredient("queijo mussarela"))
    assert Ingredient("farinha") == Ingredient("farinha")
    assert Ingredient("farinha") != Ingredient("queijo mussarela")
    assert repr(Ingredient("bacon")) == "Ingredient('bacon')"
    assert Ingredient("bacon").name == "bacon"
    assert Ingredient("bacon").restrictions != {Restriction.GLUTEN}
    assert set(Ingredient("farinha").restrictions) == {Restriction.GLUTEN}
