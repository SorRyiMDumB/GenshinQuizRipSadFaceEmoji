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
    global G

    os.system('databaseInit.py')            # excutes the database init file 
    G = nx.Graph()                                  # creates graph named G

    addnodes()

def addnodes():
    ''' adds all the nodes from the database'''
    select_users = "SELECT * from users"
    allusers = execute_read_query(connection, select_users)
    for i in allusers:
        G.add_node(
        i[0], 
        year = i[1],                # shape /////
        house = i[2],               # edge, color, outline /////
        classes = i[3],             # edge 
        genshin = i[4],                 # edge, color, outline
        uni = i[5],                 # edge
        course = i[6],              # edge
        f1 = i[7],              # edge, color, shape outline
        sport = i[8],               # edge, shape color outline
        tutorMath = i[9],               # edge
        tutorEng = i[10],               # edge
        tutorHums = i[11],              # edge
        tutorScience = i[12],               # edge
        friends = i[13]                 # size 
        )


### CREATORS
def node_con_exist(param,given_colour,given_weight):
    ''' 
    Connects all nodes where data is present in the param given.
    
    ### EXAMPLE USAGE
    All nodes with param = food will be connected 
        and given atributes colour = given colur and weight = given_weight

    '''

    worklist = []               # creates a working list

    for node, data in G.nodes(data=True): # checks if data param is present in the graph
        if data[param] != "0":              # checks if the data exists 
            worklist.append(node)               #adds node to working list
    print(param, worklist)

    while len(worklist) != 0:               # runs until the list is empty
        for i in worklist:
            if i == worklist[0]:
                pass
            else:
                G.add_edge(i,worklist[0],colour= given_colour,weight= given_weight)             # connects nodes in working list with atributes
        worklist.pop(0)

def node_con_test(param,testcase,given_colour,given_weight):
    ''' 
    Connects all nodes where data is equal to test case given.

    ### EXAMPLE USAGE 
    All nodes with param = food and testcase = burger will be connected
        and given atributes colour = given colur and weight = given_weight
    '''

    worklist = []               # creates a working list

    for node, data in G.nodes(data=True):               # checks if data param is present in the graph
        if data[param] == testcase:             # checks if the data retrieved is equal to test case
            worklist.append(node)               # adds node to working list

    while len(worklist) != 0:               # runs until the list is empty 
        for i in worklist:
            if i == worklist[0]:                # if the list is empty the function is ended 
                pass
            else: 
                G.add_edge(i,worklist[0],colour= given_colour,weight= given_weight)             # creates edges to all nodes and adds atributes
        worklist.pop(0)

def attributor(param,testcase,atri,atri_data):
    '''
    Gives all nodes with atribute "param", that equal to a testcase "testcase", a new atribute "arti" with data "atri_data"

    '''

    worklist = []

    for node, data in G.nodes(data=True):               # checks if data param is present in the graph
        if data[param] == testcase:             # checks if the data retrieved is equal to test case
            worklist.append(node)
    
    while len(worklist) != 0:               # runs until the list is empty 
        for i in worklist:
            if i == worklist[0]:                # if the list is empty the function is ended 
                pass
            else:
                G.nodes[worklist[0]][atri] = atri_data
        worklist.pop(0)


### NODE GENERATION
def year_node():
    attributor("year","11","shape","triangle")
    attributor("year","12","shape","circle")

def house_node(type):
    '''
    Draws graph where all student in same house are connected.
    
    ### TYPE
    if type = colour then node will be given an attribute named colour based on house
        if type = outline then node will be given an attribute named outline based on house
    '''
    
    if type == "colour":
        attributor("house","R","colour","yellow")
        attributor("house","K","colour","red")
        attributor("house","B","colour","blue")
        attributor("house","C","colour","green")
    
    if type == "outline":
        attributor("house","R","outline","yellow")
        attributor("house","K","outline","red")
        attributor("house","B","outline","blue")
        attributor("house","C","outline","green")


### EDGE GENERATION
def house_edge():
    '''
    Draws graph where all student in same house are connected.
    '''

    node_con_test("house","R","yellow","1")
    node_con_test("house","B","blue","1")
    node_con_test("house","C","green","1")
    node_con_test("house","K","red","1")

def                     classes_edge():
    '''
    Draws graph where all student in same classes
    '''
    pass

def uni_edge():
    '''
    Draws graph where all student who want the same uni are connected.
    '''
    node_con_test("uni","MEL", "purple","1")
    node_con_test("uni","MON", "blue", "1")
    node_con_test("uni","RMIT", "red", "1")

def course_edge():
    '''
    Draws graph where all student who want the same course are connected.
    '''
    node_con_test("course","COM", "blue","1")
    node_con_test("course","FIN", "green","1")
    node_con_test("course","MED", "red","1")
    node_con_test("course","ENG", "black","1")
    node_con_test("course","ART", "pink","1")
    node_con_test("course","LAW", "yellow","1")

def f1_edge():
    '''
    Draws graph where all student who like f1 connected.
    '''

    node_con_exist("f1","red","1")
    
def genshin_edge():
    '''
    Draws graph where all student play genshin are connected.
    '''

    node_con_exist("genshin","pink","1")

def tutor_edge():
    '''
    Draws graph where all student who do tutoring are connected.
    '''
    node_con_exist("tutorEng","pink","1")
    node_con_exist("tutorMath","blue","1")
    node_con_exist("tutorHums","red","1")
    node_con_exist("tutorScience","green","1")

def sport_edge():
    '''
    Draws graph where all student who do tutoring are connected.
    '''

    node_con_test("sport","BBALL", "yellow","1")
    node_con_test("sport","SWIM", "blue","1")
    node_con_test("sport","CRICKET", "green","1")
    node_con_test("sport","MMA", "red","1")
    node_con_test("sport","NETBALL", "pink","1")
    node_con_test("sport","TENNIS", "orange","1")

### RUNNING
init()
sport_edge()
house_edge()

#print(nx.nodes(G))

pos = nx.spring_layout(G, seed=12345)

edgecolor = nx.get_edge_attributes(G, 'colour').values()
nodesize = nx.get_node_attributes(G, 'weight').values()
nodecolour = nx.get_node_attributes(G, 'colour').values()

#nodes = nx.draw_networkx_nodes (G, pos, node_size=nodesize, node_color=nodecolour)
edges = nx.draw_networkx_edges(G, pos, width=1, edge_color=edgecolor)
#nx.draw_networkx(G,pos)

house_node("colour")
print(G.nodes[1])

plt.show()

