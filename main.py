import pandas as pd

from .explorator import Explorator
from edge import Edge

CSV_Path = 'parcours_explorateurs.csv'

def prepare_data(explorator_df):

    adjacency_table = {}
    for _, row in explorator_df.iterrows():
        upstream_node = row["noeud_amont"]
        downstream_node = row["noeud_aval"]
        distance = row["distance"]
        edge_type = row["type_aretes"]
        edge_id = row["arete_id"]

        edge_object = Edge(upstream_node, downstream_node, distance, edge_type, edge_id)
        adjacency_table[upstream_node] = edge_object
    
    departs = explorator_df[explorator_df['type_aretes'] == 'depart']\
                                ['noeud_amont'].values
    
    finishes = set(explorator_df[explorator_df['type_aretes'] == 'arrivee']\
                                ['noeud_aval'].values)
    
    # print(departs) # test print departs
    # print(finishes) # test print finishes
    
    return adjacency_table, departs, finishes
    
def find_explorator_path(adjacency_table, departs, finishes):

    for depart_node in departs:          # for each depart node
        current_path = [depart_node]     # initialize path with depart node
        current_node = current_path[-1]  # get information about current position of the explorer
        distance = 0                     # initialize distance traveled
        
        # while explorer has not reached finish
        while current_node not in finishes:             
            # get to next node/ current journey
            next_node, current_distance = adjacency_table[current_node]   
            # stock the node where explorer is at the end of the day
            current_path.append(next_node)              
            # actualize distance traveled
            distance += current_distance                 
            # actualize current position of the explorer
            current_node = current_path[-1]             

        # find the longest path and print it
        

        print(f"Path found: {current_path} starting with {current_path[0]}, ending with {current_path[-1]} and total distance {distance:<.3f} kms.")
    

# Main execution
## Load data
explorator_df = pd.read_csv(CSV_Path)
## Prepare data
adjacency_table, departs, finishes = prepare_data(explorator_df)
### Find paths
find_explorator_path(adjacency_table, departs, finishes)

