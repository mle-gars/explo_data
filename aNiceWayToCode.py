
import pandas as pd
from collections import defaultdict
from typing import Dict, List, Tuple

CSV_Path = 'parcours_explorateurs.csv'

explorator_df = pd.read_csv(CSV_Path)
# print (explorator_df.head()) # test print

####################################

adjacency_table = {}

# for index_row, row in explorator_df.iterrows():
    
    # if row['type_aretes'] == 'depart':
    # if row['type_aretes'] == 'arrivee':
    # print(index_row, row['arete_id'], row['type_aretes'], row['distance'], "km")

#    adjacency_table[row["noeud_amont"]] = row["noeud_aval"]

adjacency_table = {row["noeud_amont"]: row["noeud_aval"]\
                    for _, row in explorator_df.iterrows()}

####################################

departs = explorator_df[explorator_df['type_aretes'] == 'depart'].to_numpy()
finishes = explorator_df[explorator_df['type_aretes'] == 'arrivee'].to_numpy()

print(departs) # test print departs
print(finishes) # test print finishes

