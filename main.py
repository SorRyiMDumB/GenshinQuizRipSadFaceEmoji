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
        classes = i[3],             # edge 
        genshin = i[4],                 # edge, color, outline /////
        uni = i[5],                 # edge /////
        course = i[6],              # edge /////
        f1 = i[7],              # edge, shape outline /////
        sport = i[8],               # edge, color outline /////
        tutorMath = i[9],               # edge 
        tutorEng = i[10],               # edge 
        tutorHums = i[11],              # edge 
        tutorScience = i[12],               # edge 
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

def conn_test(param : str, colors : list, weights : list, labels : list):
    """ Connects nodes that share the same parameter

    Args:
        param (str): Parameter to be checked 
        colors (list): List of colours to give the nodes
        weights (list): List of weights to give the nodes
        labels (list): List of colours to give the nodes
    """

    # List of unique values in the parameter 
    uniqueVal = []

    # for every node in the graph 
    for node in G:
        # find the data assoicated with the parameter 
        nodedata = G.nodes[node][param]
        
        # if the data found is already in the unique value list, skip 
        if nodedata in uniqueVal:
            pass
        
        # if data is not in unique value list, add data point
        else:
            uniqueVal.append(nodedata)
    
    # prints out statement saying what the unique values are in the parameter after all nodes have been searched
    if "0" in uniqueVal:
        uniqueVal.remove("0")
    print("#####################\nThe unique values in parameter: ",param, " are ", uniqueVal)

    # creates a simple counter to go through the lists provided to make sure the proper data is added to edges
    listcounter = 0

    # for every value in the unique value list 
    for testcase in uniqueVal:
        # reset the worklist everytime we test a new varible 
        worklist = []

        # for every node in the graph 
        for node in G:
            # find the data assioated with the parameter 
            nodedata = G.nodes[node][param]

            # if nodedata is the same as the varible we are testing against, add node to working list
            if nodedata == testcase:
                worklist.append(node)
            
            else:
                pass
        
        # prints out a statement of which nodes are geting what attributes added to them 
        print("\nValue: ", testcase, " has nodes: ", worklist, "  |  index number is",listcounter,
        "\nColor:", colors[listcounter], "| Weight:", weights[listcounter], " | Label:", labels[listcounter])
        
        # while the working list contains nodes
        while len(worklist) != 0:
            # for every node in that working list

            for node in worklist:

                # if the node is the first item, skip
                if node == worklist[0]:
                    pass
                
                # connects an edge from the node and the first node on the working list, also assigns the artibutes 
                else:
                    G.add_edge(
                    node,
                    worklist[0],
                    colour = str(colors[listcounter]),
                    weight= weights[listcounter],            # connects nodes in working list with atributes
                    label = str(labels[listcounter])
                    )
            # removes node that was just used to make a connection 
            worklist.pop(0)
        
        # adds one to list counter so next time algo runs it uses next data
        listcounter = listcounter + 1

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

def cheesyfunc(cheese):
    cheeseholder = []

    cheesebutwithcream = nx.get_node_attributes(G, cheese).values()
    for i in cheesebutwithcream:
        cheeseholder.append(i)
    return cheeseholder

### NODE GENERATION
def year_node():
    '''
    Attributes nodes with a shape depending on their year level
    '''
    attributor("year",11,"shape","^")
    attributor("year",12,"shape","o")

def house_node(type):
    '''
    Attributes nodes with a outline/colour depending on their house
    '''
    
    if type == "node_color":
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
        attributor("sport", "CRICKET", "colour",str(color[2]))
        attributor("sport","MMA", "colour",str(color[3]))
        attributor("sport","NETBALL", "colour",str(color[4]))
        attributor("sport","TENNIS", "colour",str(color[5]))
    
    if type == "outline":
        attributor("sport","BBALL","outline", str(color[0]))
        attributor("sport","SWIM", "outline", str(color[1]))
        attributor("sport","CRICKET", "outline", str(color[2]))
        attributor("sport","MMA", "outline", str(color[3]))
        attributor("sport","NETBALL", "outline", str(color[4]))
        attributor("sport","TENNIS", "outline",str(color[5]))

    print("BBALL[0], SWIM[1], CRICKET[2], MMA[3], NETBALL[4], TENNIS[5]")
    print(color)

### EDGE GENERATION

def classes_edge(given_colour):
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


def f1_edge():
    '''
    Draws graph where all student who like f1 connected.
    '''

    node_con_exist("f1","red","1")



### INIT
init()

### ADD GRAPH ELEMENTS HERE

#house_node("node_color")

classes_edge("black")
#sport_node("outline",["yellow","blue", "green", "red", "gold", "lime"])
#sport_node("colour", ["pink","pink", "pink", "pink", "pink", "pink"])
#sport_edge()
#course_edge()

#conn_test('year', ["purple", "pink"], [1, 1], ["12", "11"])

#conn_test('house', ["blue", "yellow", "green", "red"], [1, 1, 1, 1], ["Blackwood", "Rothwell", "Cotrell", "Kororoit"])

#conn_test('genshin', ["red", "green", "light green", "blue", "dark blue", "grey", "purple"], [1, 1, 1, 1, 1, 1, 1], ['Hutao', 'Venti', 'Sucrose', 'Yelan ', 'Raiden Shogun', 'Razor', 'Lisa'])

#conn_test('uni', ["blue", "turquoise", "yellow", "red", "green"], [1, 1, 1, 1, 1], ['Melbourne University', 'Monash University', 'Utrecht University', 'Royal Melbourne Institute of Technology', 'Victorian University'])

#conn_test('course', ["grey", "green", "red", "yellow", "black", "pink", "brown", "gold","blue","orange"], [1,1,1,1,1,1,1,1,1,1,1], ['COM', 'FIN', 'MED', 'LIT', 'ENG', 'ART', 'PSY', 'LAW', 'SCI', 'MUS'] ) 

#conn_test('f1', ["orange", "blue", "yellow", "light blue", "green", "red"], [1, 1, 1, 1, 1, 1], ['MCLAREN', 'RED BULL', 'HAAS', 'WILLIAMS', 'ALFA ROMEO', 'FERRARI'])

#conn_test('sport', ["yellow","blue", "green", "red", "gold", "lime"], [1, 1,1,1,1,1,1,1,1], ['BBALL', 'SWIM', 'CRICKET', 'MMA', 'NETBALL', 'TENNIS'])

### GRAPH DRAWING
def draw_graph(cheese):
    # position of nodes
    pos = nx.spring_layout(G, seed = 42)               
    
    # drawing nodes
    for node in G:
        worklist = [node]
        x = int(G.nodes[node]['weight'])
        sizeX = (0.02 * ((x) ** 2)) + (8.6 * x) + 411.1
        nx.draw_networkx_nodes(
            G,
            pos,
            nodelist = worklist,
            node_size = float(sizeX),
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

    if cheese == "weighted":
        edgelabels = {}
        for n1, n2, data in G.edges.data():
            edgelabels[(n1, n2)] = data['weight']
            print(n1,n2,data['weight'])
        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=edgelabels,
            font_size=7
        )

    if cheese == "labeled":
        edgelabels = {}
        for n1, n2, data in G.edges.data():
            edgelabels[(n1, n2)] = data['label']
        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=edgelabels,
            font_size=7
        )

    else:
        pass

    plt.show()
#raw_graph("weight")

draw_graph('weighted')
print("\n")
