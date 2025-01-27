# Author: Alec Krsek
# Description: This script generates an ER diagram for the database schema

from graphviz import Digraph


diagram = Digraph("Aiport EER Diagram", format="png")
diagram.attr(rankdir="TB")

# Entities with their attributes
entities = {
    "Airplane": ["Rnum"],
    "PlaneType": ["Model", "Year", "Capacity", "Location"],
    "Hangar": ["Hnum", "Capacity", "Location", "Hyear"],
    "Maintenance": ["Date", "Workcode", "Hours", "Cost"],
    "Owner": [],

}

# Loop to add the entities to the diagram
for entity, attributes in entities.items():
    label = f"<<TABLE BORDER='0' CELLBORDER='1' CELLSPACING='0'>"
    label += f"<TR><TD COLSPAN='1'><B>{entity}</B></TD></TR>"
    for attr in attributes:
        label += f"<TR><TD>{attr}</TD></TR>"
    label += "</TABLE>>"
    diagram.node(entity, label=label, shape="plaintext")


# Relationships
relationships = {
    "OF-TYPE": ("Airplane", "PlaneType"),
    "STORED-IN": ("Airplane", "Hangar"),
    "OWNS": ("Airplane", "Owner"),
    "MAINTAIN":("Employee", "Maintenance"),
    "PLANE-MAINTAINCE": ("Airplane", "Maintenance"),

}

# Add relationships to the diagram
for rel, (from_ent, to_ent), in relationships.items():
    diagram.node(rel, rel, shape="diamond")
    diagram.edge(from_ent, rel)
    diagram.edge(rel, to_ent)

# Specializations and Generalizations
diagram.node("Person", "Person", shape="ellipse")

# Unions
diagram.node("OwnerUnion", "U", shape="circle")

# Add the diagram to the file
file_path = "eer-diagram"
diagram.render(file_path, cleanup=True)

