# Author: Alec Krsek
# Description: This script generates an ER diagram for the database schema

from graphviz import Digraph


diagram = Digraph("Aiport EER Diagram", format="png")
diagram.attr(rankdir="LR")

# Entities with their attributes
entities = {
    "Airplane": ["Rnum"],
}

# Loop to add the entities to the diagram
for entity, attributes in entities.items():
    diagram.node(entity, f"{entity}\n{attributes}")


# Relationships
relationships = {
    "OF-TYPE": ("Airplane", "PlaneType"),
    "STORED-IN": ("Airplane", "Hangar"),
}

# Add relationships to the diagram
for rel, (from_ent, to_ent), in relationships.items():
    diagram.edge(from_ent, to_ent, label=rel)

# Specializations and Generalizations
diagram.node("Person", "Peson\nPid, name, Address, Phone, Dob", shape="ellipse")

# Union for Owner
diagram.node("Owner", "Owner", shape="ellipse")

# Add the diagram to the file
file_path = "eer-diagram"
diagram.render(file_path, cleanup=True)

