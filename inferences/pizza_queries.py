import owlready2 as owl
from owlready2.reasoning import sync_reasoner

friends = owl.get_ontology("../Ontologies/friend_with_eating_habits.owl")
friends.load()
pizza = owl.get_ontology("../Ontologies/pizza_protege.owl")
pizza.load()



