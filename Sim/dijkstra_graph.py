#seedhu is very unstudious
import networkx as nx
import matplotlib.pyplot as plt

# Define the organs in the digestive system
digestive_organs = [
    "Oral Cavity", "Pharynx", "Esophagus", "Stomach",
    "Small Intestine", "Large Intestine", "Rectum", "Anus"
]

# Define the organs in the respiratory system
respiratory_organs = [
    "Nasal Cavity", "Sinuses", "Pharynx", "Larynx",
    "Trachea", "Bronchi", "Lungs"
]

# Create an empty graph
G = nx.Graph()

# Add nodes for each organ in the digestive system
for organ in digestive_organs:
    G.add_node(organ)

# Add nodes for each organ in the respiratory system
for organ in respiratory_organs:
    G.add_node(organ)

# Define connections and distances (in cm) between digestive organs
digestive_edges = [
    ("Oral Cavity", "Pharynx", 2.5),        # Average distance 2.5 cm
    ("Pharynx", "Esophagus", 5.5),         # Average distance 5.5 cm
    ("Esophagus", "Stomach", 12.5),        # Average distance 12.5 cm
    ("Stomach", "Small Intestine", 7.5),    # Average distance 7.5 cm
    ("Small Intestine", "Large Intestine", 3.5), # Average distance 3.5 cm
    ("Large Intestine", "Rectum", 17.5),    # Average distance 17.5 cm
    ("Rectum", "Anus", 3.0)                 # Average distance 3.0 cm
]

# Define connections and distances (in cm) between respiratory organs
respiratory_edges = [
    ("Nasal Cavity", "Pharynx", 10),        # Average distance 10 cm
    ("Sinuses", "Pharynx", 5),              # Average distance 5 cm
    ("Pharynx", "Larynx", 2),               # Average distance 2 cm
    ("Larynx", "Trachea", 1),               # Average distance 1 cm
    ("Trachea", "Bronchi", 2),              # Average distance 2 cm
    ("Bronchi", "Lungs", 1)                 # Average distance 1 cm
]

# Add edges with weights to the graph for digestive organs
G.add_weighted_edges_from(digestive_edges)

# Add edges with weights to the graph for respiratory organs
G.add_weighted_edges_from(respiratory_edges)

# Define connections between digestive and respiratory systems
cross_system_edges = [
    ("Oral Cavity", "Nasal Cavity", 5),     # Average distance 5 cm
    ("Pharynx", "Larynx", 2),               # Already included
]

# Add cross-system edges
G.add_weighted_edges_from(cross_system_edges)

# Set positions for nodes using a circular layout
pos = nx.circular_layout(G)

# Draw the graph with edges showing weights
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_color='black', font_weight='bold', edge_color='gray')

# Draw edge labels to show distances
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels={k: f"{v} cm" for k, v in edge_labels.items()})

plt.title("Digestive and Respiratory System Organs with Distances (in cm)")
plt.show()
