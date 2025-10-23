import pandas as pd

CSV_Path = 'parcours_explorateurs.csv'

"""
def prepare_data(explorator_df):

    adjacency_table = {row["noeud_amont"]: (row["noeud_aval"], row["distance"])\
                        for _, row in explorator_df.iterrows()}
    
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

"""


class Explorator:
    def __init__ (self, start_node):
        self.current_node = start_node
        self.path = [start_node]
        self.total_distance = 0

    def __repr__(self):
        return f"Explorator at node {self.current_node} with path {self.path} \
                    and total distance {self.total_distance}"

    def move_to(self, next_node, distance):
        self.current_node = next_node
        self.path.append(next_node)
        self.total_distance += distance

class PathFinder:
    def __init__(self, adjacency_table, departs, finishes):
        self.adjacency_table = adjacency_table
        self.departs = departs
        self.finishes = finishes

    def find_explorator_path(self):
        for depart_node in self.departs:
            explorer = Explorator(depart_node)
            while explorer.current_node not in self.finishes:
                next_node, current_distance = self.adjacency_table[explorer.current_node]
                explorer.move_to(next_node, current_distance)

            print(f"Path found: {explorer.path} starting with {explorer.path[0]}, \
                    ending with {explorer.path[-1]} and total distance {explorer.total_distance:<.3f} kms.")