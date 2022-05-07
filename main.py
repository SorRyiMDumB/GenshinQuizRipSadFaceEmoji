#bruh

### IMPORTS
# Database
import sqlite3

from numpy import append

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
        classes = i[3],             # edge /////
        genshin = i[4],                 # edge, color, outline /////
        uni = i[5],                 # edge /////
        course = i[6],              # edge ///// 
        f1 = i[7],              # edge, shape outline ///// 
        sport = i[8],               # edge, color outline ///// 
        tutorMath = i[9],               # edge ///// 
        tutorEng = i[10],               # edge ///// 
        tutorHums = i[11],              # edge ///// 
        tutorScience = i[12],               # edge ///// 
        friends = i[13],                 # size
        
        colour = "white",
        weight = "1",
        shape = "o",
        outline = "black"
        )


### CREATORS
def node_con_exist(param,given_colour,given_weight):
    """Connects all nodes where data is present in the param given.

    ### Args:
        param (string): connects if param is true
        given_colour (string): what the color of node should be
        given_weight (float): what the wieght of the node should be
    """

    worklist = []               # creates a working list

    for node, data in G.nodes(data=True): # checks if data param is present in the graph
        if data[param] != "0":              # checks if the data exists 
            worklist.append(node)               #adds node to working list

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

    ### EXAMPLE USAGE 
    All nodes with param = food and testcase = burger will be connected
        and given atributes colour = given colur and weight = given_weight

    '''

    worklist = []

    for node in G:               # checks if data param is present in the graph
        if G.nodes[node][param] == testcase:
            worklist.append(node)
        else:
            pass

    print("List that satisfy", testcase, "are: ", worklist)

    for i in worklist:
        # i = nodes that statfiy condition
        G.nodes[i][atri] = atri_data

def cheesyfunc(arti):
    list = []

    cheese = nx.get_node_attributes(G, arti).values()
    for i in cheese:
        list.append(i)
    return list

### NODE GENERATION
def year_node():
    '''
    Attributes nodes with a shape depending on their year level
    '''
    attributor("year","11","shape","triangle")
    attributor("year","12","shape","circle")

def house_node(type):
    '''
    Attributes nodes with a outline/colour depending on their house
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

def genshin_node(type,color):
    '''
    Attributes nodes with a colour/outline depending on if they play genshinn
    '''
    
    if type == "colour":
        attributor("genshin",True,"colour",color)
    
    if type == "outline":
        attributor("genshin",True,"outline",color)

def f1_node(type,color):
    
    if type == "shape":
        attributor("f1",True,"shape",color)
    
    if type == "outline":
        attributor("f1",True,"outline",color)

def sport_node(type, color : list):
    """Attributes nodes with a color/outline based on their sport

    ### Args:
        type (str): what atribute to modify
        color (list): list containing the colors to change it to

    ### List order
        BBALL[0], SWIM[1], CRICKET[2], MMA[3], NETBALL[4], TENNIS[5]
    """
    
    if type == "colour":
        attributor("sport","BBALL","colour",str(color[0]))
        attributor("sport","SWIM", "colour",str(color[1]))
        attributor("sport","CRICKET", "colour",str(color[2]))
        attributor("sport","MMA", "colour",str(color[3]))
        attributor("sport","NETBALL", "colour",str(color[4]))
        attributor("sport","TENNIS", "colour",str(color[5]))
    
    if type == "outline":
        attributor("sport","BBALL","colour",color)
        attributor("sport","SWIM", "colour",color)
        attributor("sport","CRICKET", "colour",color)
        attributor("sport","MMA", "colour",color)
        attributor("sport","NETBALL", "colour",color)
        attributor("sport","TENNIS", "colour",color)


### EDGE GENERATION
def house_edge():
    '''
    Draws graph where all student in same house are connected.
    '''

    node_con_test("house","R","yellow","1")
    node_con_test("house","B","blue","1")
    node_con_test("house","C","green","1")
    node_con_test("house","K","red","1")

def classes_edge(given_colour,):
    for node in G:
        raw = G.nodes[node]["classes"]
        worklist = raw.split("~")
        
        for testnode in G:
            if node == testnode:
                pass
            else:
                testraw = G.nodes[testnode]["classes"]
                testworklist = testraw.split("~")
                a = set(testworklist).intersection(worklist)
                if len(a) == 0:
                    pass
                else:
                    G.add_edge(node,testnode,colour= given_colour,weight= len(a))

def genshin_edge():
    '''
    Draws graph where all student play genshin are connected.
    '''

    node_con_exist("genshin","pink","1")

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

def tutor_edge():
    '''
    Draws graph where all student who do tutoring are connected.
    '''
    node_con_exist("tutorEng","pink","1")
    node_con_exist("tutorMath","blue","1")
    node_con_exist("tutorHums","red","1")
    node_con_exist("tutorScience","green","1")


### INIT
init()

### ADD GRAPH ELEMENTS HERE

#sport_node("colour",["yellow","blue", "green", "red", "gold", "lime"])
#genshin_edge()
#nodesize = nx.get_node_attributes(G, 'weight').values()
classes_edge("black")

### GRAPH DRAWING
def draw_graph():
    # position of nodes
    pos = nx.spring_layout(G, seed=42)               
    
    # drawing nodes
    for node in G:
        worklist = [node]
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist = worklist,
            node_size = (int(G.nodes[node]['weight']) * 500),
            node_color = G.nodes[node]['colour'],
            node_shape = G.nodes[node]["shape"],
            edgecolors = G.nodes[node]["outline"],
            label = node
        )
        nx.draw_networkx_labels(
            G,
            pos,
            font_size=12,
        )

    # drawing edges
    edgecolor = nx.get_edge_attributes(G, 'colour').values()

    nx.draw_networkx_edges(
        G,
        pos,
        width=1,
        edge_color=edgecolor
    )

    edgelabels = {}
    for n1, n2, data in G.edges.data():
        edgelabels[(n1, n2)] = data['weight']
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=edgelabels,
        font_size=7
    )
    

    #print(G.nodes[11])

    plt.show()
draw_graph()