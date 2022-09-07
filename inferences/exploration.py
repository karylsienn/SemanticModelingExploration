import rdflib
import owlready2 as owl
import owlready2.reasoning as reasoning

ontology = owl.get_ontology("../Ontologies/ontology.rdf")
ontology.load()

prefixes_for_queries = """
PREFIX ppl: <http://cohse.semanticweb.org/ontologies/people#>
"""

# People namespace
people = ontology.get_namespace("http://cohse.semanticweb.org/ontologies/people")  # Note without '#' in the end

# Let's search for anything that has a pet: equivalent to ?subject has_pet ?object
owners_and_pets_query = prefixes_for_queries + """
SELECT * WHERE {
    ?object ppl:has_pet ?instance
}
"""
owners_and_pets = list(ontology.world.sparql(owners_and_pets_query))
print("There are %d owners that have pets." % len(owners_and_pets))

# Let's search for the inverse relationship
pets_and_owners_query = prefixes_for_queries + """
SELECT * WHERE {
    ?pet ppl:is_pet_of ?owner
}
"""
pets_and_owners = list(ontology.world.sparql(pets_and_owners_query))
print("There are %d pets that have owners." % len(pets_and_owners))

# Now let's see if there is the "likes" property
owner_likes_pet_query = prefixes_for_queries + """
SELECT * WHERE {
    ?object ppl:likes ?subject
}
"""
owner_likes_pet = list(ontology.world.sparql(owner_likes_pet_query))  # Should be nothing
print("There are %d owners that like anyone." % len(owner_likes_pet))

# 'likes' has subclass 'has_pet'
print("%s has the following super classes %s." % (people.has_pet, str(list(people.has_pet.is_a))))

# However, the list of owners liking their pets is empty. It should not be after launching reasoner.
reasoning.sync_reasoner_pellet(ontology, infer_property_values=True, infer_data_property_values=True, debug=0)

# Let's find out now
owner_likes_pet_after_reasoning = list(ontology.world.sparql(owner_likes_pet_query))
print("After reasoning: there are %d owners that like anyone." % len(owner_likes_pet_after_reasoning))
print("After reasoning: there are %d owners that have pets." % len(list(ontology.world.sparql(owners_and_pets_query))))
print("After reasoning: there are %d pets that have owners." % len(list(ontology.world.sparql(pets_and_owners_query))))
