import pandas as pd

CSV_Path = 'parcours_explorateurs.csv'

class Explorator:
    def __init__ (self):
        self.path = []

    def move_to(self, next_node, distance):
        self.path.append(distance)  

    def get_total_distance(self):
        return sum(self.path)
    
