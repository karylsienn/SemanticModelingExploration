import owlready2 as owl
import owlready2.reasoning as reason

"""
This is an exercise from ProtegeOWL Tutorial. Instead of making that in protege I made it here.
"""

pizza_onto = owl.get_ontology("http://semanticweb.org/karolniewiadomski/ontologies/pizza.owl")
pizza = pizza_onto.get_namespace("http://semanticweb.org/karolniewiadomski/ontologies/pizza")

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


    class DeepPanBase(PizzaBase):
        pass


    owl.AllDisjoint([DeepPanBase, ThinAndCrispyBase])


    # # We can do it apart from "with" statement
    # class DeepPanBase(pizza_onto.PizzaBase):
    #     namespace = pizza_onto  # and then add the namespace here.
    #

    # Create meat toppings
    # with pizza_onto:
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
    # with pizza_onto:
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
    # with pizza_onto:
    class MozzarellaTopping(CheeseTopping):
        pass


    class ParmezanTopping(CheeseTopping):
        pass


    owl.AllDisjoint([MozzarellaTopping, ParmezanTopping])


    # Seafood toppings
    # with pizza_onto:
    class TunaTopping(SeafoodTopping):
        pass


    class AnchovyTopping(SeafoodTopping):
        pass


    class PrawnTopping(SeafoodTopping):
        pass


    owl.AllDisjoint([TunaTopping, AnchovyTopping, PrawnTopping])


    # Create some properties
    # with pizza_onto:
    class hasIngredient(owl.ObjectProperty):
        is_transitive = True  # After inference the property isIngredientOf will also be transitive

    class hasTopping(hasIngredient, Pizza >> PizzaTopping):
        pass

    class hasBase(hasIngredient, Pizza >> PizzaBase):
        allows_multiple_values = True


    class isIngredientOf(owl.ObjectProperty):
        inverse_property = hasIngredient


    class isBaseOf(owl.ObjectProperty, PizzaBase >> Pizza):
        inverse_property = hasBase


    class isToppingOf(owl.ObjectProperty, PizzaTopping >> Pizza):
        inverse_property = hasTopping  # after launching reasoner this is now a subclass of isIngredientOf -- cool.

# Adding the restrictions afterwards
Pizza.is_a.append(hasTopping.some(PizzaBase))

# Creating more subclasses
with pizza_onto:
    class NamedPizza(Pizza):
        pass

    class MargheritaPizza(NamedPizza):
        comment = ["A pizza that only has Mozarella and Tomato toppings"]
        is_a = [hasTopping.some(MozzarellaTopping) & hasTopping.some(TomatoTopping)]

    class AmericanaPizza(NamedPizza):
        comment = ["A pizza that has Mozarella, Tomato and Pepperoni toppings."]
        is_a = [hasTopping.some(MozzarellaTopping) & hasTopping.some(TomatoTopping) &
                hasTopping.some(PepperoniTopping)]

    class AmericanHotPizza(NamedPizza):
        comment = ["Americana with Jalapeno."]
        is_a = [hasTopping.some(MozzarellaTopping) & hasTopping.some(TomatoTopping) &
                hasTopping.some(PepperoniTopping) & hasTopping.some(JalapenoPepperTopping)]

    class SohoPizza(NamedPizza):
        comment = ["Margherita with olives and parmezan."]
        is_a = [hasTopping.some(MozzarellaTopping) & hasTopping.some(TomatoTopping) &
                hasTopping.some(OliveTopping) & hasTopping.some(ParmezanTopping)]

    owl.AllDisjoint([MargheritaPizza, AmericanaPizza, AmericanHotPizza, SohoPizza])


# Create an inconsistent class
with pizza_onto:
    class ProbeInconsistentTopping(CheeseTopping):
        comment = ["A class for checking inconsistent ontology."]
        is_a = [VegetableTopping]  # Should be inconsistent as a subclass of cheese topping.

owl.close_world(pizza_onto)

reason.sync_reasoner(pizza_onto)



