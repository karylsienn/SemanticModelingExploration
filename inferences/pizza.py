import owlready2 as owl

pizza_onto = owl.get_ontology("http://semanticweb.org/karolniewiadomski/ontologies/pizza.owl")

with pizza_onto:
    class Pizza(owl.Thing):
        pass

    class PizzaTopping(owl.Thing):
        pass

    class PizzaBase(owl.Thing):
        pass

    owl.AllDisjoint([Pizza, PizzaBase, PizzaTopping])

    class ThinAndCrispyBase(PizzaBase):
        pass

    # Toppings
    class MeatTopping(PizzaTopping):
        pass

    class VegetableTopping(PizzaTopping):
        pass

    class CheeseTopping(PizzaTopping):
        pass

    class SeafoodTopping(PizzaTopping):
        pass

    owl.AllDisjoint([MeatTopping, VegetableTopping, CheeseTopping, SeafoodTopping])


# We can do it apart from "with" statement
class DeepPanBase(pizza_onto.PizzaBase):
    namespace = pizza_onto  # and then add the namespace here.


# Create meat toppings
with pizza_onto:
    class SpicyBeefTopping(MeatTopping):
        pass

    class PepperoniTopping(MeatTopping):
        pass

    class SalamiTopping(MeatTopping):
        pass

    class HamTopping(MeatTopping):
        pass

    owl.AllDisjoint([SpicyBeefTopping, PepperoniTopping, SalamiTopping, HamTopping])


# Vegetable toppings
with pizza_onto:
    class TomatoTopping(VegetableTopping):
        pass

    class OliveTopping(VegetableTopping):
        pass

    class MushroomTopping(VegetableTopping):
        pass

    class PepperTopping(VegetableTopping):
        pass

    class OnionTopping(VegetableTopping):
        pass

    class CaperTopping(VegetableTopping):
        pass

    owl.AllDisjoint([TomatoTopping, OliveTopping, MushroomTopping, PepperTopping, OnionTopping, CaperTopping])

    class RedPepperTopping(PepperTopping):
        pass

    class GreenPepperTopping(PepperTopping):
        pass

    class JalapenoPepperTopping(PepperTopping):
        pass

    owl.AllDisjoint([RedPepperTopping, GreenPepperTopping, JalapenoPepperTopping])

# Cheese toppings
with pizza_onto:
    class MozzarellaTopping(CheeseTopping):
        pass

    class ParmezanTopping(CheeseTopping):
        pass

    owl.AllDisjoint([MozzarellaTopping, ParmezanTopping])


# Seafood toppings
with pizza_onto:
    class TunaTopping(SeafoodTopping):
        pass

    class AnchovyTopping(SeafoodTopping):
        pass

    class PrawnTopping(SeafoodTopping):
        pass

    owl.AllDisjoint([TunaTopping, AnchovyTopping, PrawnTopping])


# Create some properties
with pizza_onto:
    class hasIngredient(owl.ObjectProperty):
        pass

    class hasTopping(hasIngredient):
        pass

    class hasBase(hasIngredient):
        pass

    class isIngredientOf(owl.ObjectProperty):
        inverse_property = hasIngredient

    class isBaseOf(owl.ObjectProperty):
        inverse_property = hasBase

    class isToppingOf(owl.ObjectProperty):
        inverse_property = hasTopping  # after launching reasoner this is now a subclass of isIngredientOf -- cool.

