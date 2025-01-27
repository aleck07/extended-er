# Author: Alec Krsek
# Description: This script generates an ER diagram for the database schema

from graphviz import Digraph


diagram = Digraph("Aiport EER Diagram", format="png")
diagram.attr(rankdir="TB")

# Entities with their attributes
entities = {
    "Airplane": ["<U>Rnum</U>"],
    "PlaneType": ["Model", "Year", "Capacity", "Location"],
    "Hangar": ["<U>Hnum</U>", "Capacity", "Location", "Hyear"],
    "Maintenance": ["Date", "Workcode", "Hours", "Cost"],
    "Owner": [],
    "Company": ["<U>Ein</U>", "Name", "Address", "Phone"],
    "Person": ["<U>Pid</U>", "Name", "Address", "Phone", "Dob"],
    "Pilot": ["<U>Lnum</U>", "Plevel", "Restrict"],
    "Employee": ["Salary", "Shift", "Hdate"],

}

# Loop to add the entities to the diagram
for entity, attributes in entities.items():
    label = f"<<TABLE BORDER='0' CELLBORDER='1' CELLSPACING='0'>"
    label += f"<TR><TD COLSPAN='1'><B>{entity}</B></TD></TR>"
    for attr in attributes:
        label += f"<TR><TD>{attr}</TD></TR>"
    label += "</TABLE>>"
    diagram.node(entity, label=label, shape="none")


# Relationships
relationships = {
    "OF-TYPE": ("Airplane", "PlaneType", "1", "N"),
    "STORED-IN": ("Airplane", "Hangar", "1", "N"),
    "OWNS": ("Airplane", "Owner", "M", "N"),
    "MAINTAIN":("Employee", "Maintenance", " 1", "N"),
    "PLANE-MAINTAINCE": ("Airplane", "Maintenance", "1", "N"),
    "FLIES": ("Pilot", "PlaneType", "M", "N"),
    "WORKS-ON": ("Employee", "PlaneType", "M", "N"),
}

totalRelations= {"OWNS", "STORED-IN", "OF-TYPE", "FLIES", "WORKS-ON"}

# Add relationships to the diagram
for rel, (from_ent, to_ent, from_card, to_card), in relationships.items():
    def double_line():
        diagram.node(rel, rel, shape="diamond")
        diagram.edge(from_ent, rel, dir="none", label=f"{from_card}", penwidth="2")
        diagram.edge(rel, to_ent, dir="none", label=f"{to_card}")     
    if rel in totalRelations:
        double_line()
    else:
        diagram.node(rel, rel, shape="diamond")
        diagram.edge(from_ent, rel, dir="none", label=f"{from_card}")
        diagram.edge(rel, to_ent, dir="none", label=f"{to_card}")

# Specializations and Generalizations
diagram.node("PersonSubclass", "d", shape="circle") # The union circle with the label d
diagram.edge("Pilot", "PersonSubclass", dir="none")
diagram.edge("Employee", "PersonSubclass", dir="none")
diagram.edge("PersonSubclass", "Person", dir="none", penwidth="2")

# Unions
diagram.node("OwnerUnion", "U", shape="circle") # The union circle with the label U
diagram.edge("OwnerUnion", "Person", dir="none")
diagram.edge("OwnerUnion", "Company", dir="none")
diagram.edge("OwnerUnion", "Owner", dir="none", penwidth="2")

# Add the diagram to the file
file_path = "pyExport"
diagram.render(file_path, cleanup=True)