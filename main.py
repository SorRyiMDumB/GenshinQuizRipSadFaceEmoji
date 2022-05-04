#bruh
'''
__author__ = "Yaseen Ahmad"
__task__ = "Outcome 1,2,3"
'''

### IMPORTS
# Database
import sqlite3
import databaseInit 
from databaseInit import *

# Graphing
import networkx as nx
import matplotlib.pyplot as plt

# System
import os

### INITIALIZATION
def init():
    ''' excutes the database init file and creates a graph named G'''
    os.system('databaseInit.py')            # excutes the database init file 
    G = nx.Graph()                                  # creates graph named G

def addnodes():
    ''' adds all the nodes from the database'''
    select_users = "SELECT * from users"
    allusers = execute_read_query(connection, select_users)
    for i in allusers:
        G.add_node(
        i[0], 
        year = i[1], 
        house = i[2], 
        classes = i[3], 
        genshin = i[4], 
        uni = i[5], 
        course = i[6], 
        f1 = i[7], 
        sport = i[8], 
        tutorMath = i[9], 
        tutorEng = i[10], 
        tutorHums = i[11], 
        tutorScience = i[12], 
        friends = i[13] 
        )

for i in list(G):
    houseAtr = (G.nodes[i]["house"])
    if houseAtr == "R":
        print(G.nodes[i])


#G.add_edges([1])


nx.draw_networkx(G)
plt.show()

