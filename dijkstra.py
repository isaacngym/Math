# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:23:21 2017

@author: Isaac Ng
"""

# implementation of djikstra's algorithm
# import time  #used for time.sleep while developing
import copy

inf = 9999
    
class Edge(object):
    def __init__(self, sourcetarget, cost = 0,):
        source, target = sourcetarget.split(" ")   
        self.source = source
        self.target = target
        self.cost = cost
    def __repr__(self):
        return repr("Edge %s %s with cost %.1f" %(self.source, self.target, self.cost))
    def opp(self):
        return Edge(self.target, self.source. self.cost)
    
class Tedge(Edge):
    def __init__(self, sourcetarget, cost, timeopen = 0): #timeopen is a time that the arc is opened at
        Edge.__init__(self, sourcetarget, cost)
        self.timeopen = timeopen
   
        
#class Node(object):
#    def __init__(self, name):
#        self.name = name
        
class Network(object):
    
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        
    def fwdstar(self, node):
        star = []
        for edge in self.edges:
            if edge.source == node:
                star.append(edge)
        return star
    
    def backstar(self, node):
        star = []
        for edge in self.edges:
            if edge.target == node:
                star.append(edge)
        return star
    
    def dijkstra_iterate(self, queue, costs, preceding):
#        queue.sort(key = lambda x: x.cost) #min?
        toanalyse = min(queue, key = lambda x: costs[x])
        edgestoconsider = self.fwdstar(toanalyse)
        queue.remove(toanalyse)
        
        for edge in edgestoconsider:
            if type(edge) == Tedge:
                newcost = max(costs[edge.source], edge.timeopen) + edge.cost
            else:
                newcost = costs[edge.source] + edge.cost
            if edge.target not in queue:
                queue.append(edge.target)
            if newcost < costs[edge.target]:
                costs[edge.target] = newcost
                preceding[edge.target] = edge.source
        
        return queue, costs, preceding
    
    def dijkstra(self, source, target):
        
        queue = [source]
        costs = dict.fromkeys(self.nodes, inf)
        costs[source] = 0
        preceding = dict.fromkeys(self.nodes, None)
        while len(queue) > 0:
            self.dijkstra_iterate(queue, costs, preceding)
        return costs, preceding
    
    def shortpathneg_iterate(self, numarcs, costs, preceding):
        #costs is a dict identifying the current cost required to reach a node within <numarcs> arcs
        #preceding is a dict identifying the route to that node with that cost
        
        for edge in self.edges:
            newroute = costs[numarcs-1][edge.source] + edge.cost
            oldroute = costs[numarcs-1][edge.target]
            if newroute < oldroute: #if we can find a faster route to target
                costs[numarcs-1][edge.target] = costs[numarcs-1][edge.source] + edge.cost
                preceding[edge.target] = preceding[edge.source] + [edge.target] #update the path to that node
    
    def shortpathneg(self, source, target):
        itercosts = copy.copy(dict.fromkeys(self.nodes, inf))
        costs = dict.fromkeys(range(len(self.nodes)-1), itercosts)
        costs[0][source] = 0 #set the cost to source to be 0
        preceding = dict.fromkeys(self.nodes, [])
        for idx in range(1, len(self.nodes)):
            self.shortpathneg_iterate(idx, costs, preceding)
        finalcost = cost[len(self.nodes-1)]
        for edge in self.edges:
            if finalcost[edge.source] + edge.cost < finalcost[edge.target]:
                print "Graph has negative loop, returning one edge of aforementioned loop"
                return edge
        return costs[target], preceding
        
            
        
    def salesman_iterate(self, iteration, visited, current, costs):
        1
        
    
        
    
        
#%% test case 1    
    
    
#sa = Edge("s a", 2)
#sb = Edge("s b", 5)
#sc = Edge("s c", 3)
#ab = Edge("a b", 2)
#ad = Edge("a d", 6)
#bd = Edge("b d", 4)
#be = Edge("b e", 5)
#bt = Edge("b t", 9)
#cb = Edge("c b", 1)
#ce = Edge("c e", 1)
#de = Edge("d e", 1)
#dt = Edge("d t", 4)
#et = Edge("e t", 7)
#is there a faster way to do this?
edgeData = [['s a', 2], ['s b', 5], ['s c', 3], ['a b', 2], ['a d', 6], \
            ['b d', 4], ['b e', 5], ['b t', 9], ['c b', 1], ['c e', 1], \
            ['d e', 1], ['d t', 4], ['e t', 7]]
edges = [Edge(*[attr for attr in datapoint]) for datapoint in edgeData]


#n = Network(["s","a","b","c","d","e","t"], [sa, sb, sc, ab, ad, bd, be, bt, cb, ce, de, dt, et])
#note the extra "g" node
net = Network("s a b c d e t".split(" "), edges)
print(net.dijkstra("s", "t"))

#%% test case 2
#recitation
#abcdefgh -> 12345678
#a is source
#h is target
ab = Tedge("a b",1,0)
ac = Tedge("a c",1,1)
ad = Tedge("a d",2,1)
bc = Tedge("b c",4,0)
be = Tedge("b e",1,2)
bf = Tedge("b e",2,4)
cd = Tedge('c d',1,2)
cf = Tedge("c f",4,4)
cg = Tedge('c g',6,2)
dg = Tedge('d g',4,3)
ef = Tedge('e f',2,4)
eh = Tedge('e h',4,3)
fg = Tedge('f g',1,3)
fh = Tedge('f h',5,2)
gh = Tedge('g h',2,5)
n = Network("a b c d e f g h".split(" "), [ab,ac,ad,bc,be,bf,cd,cf,cg,dg,ef,eh,fg,fh,gh])
#note the extra "g" node
print(n.shortpathneg("a", "h"))



#%% Bellman-Ford algorithm


#%% optimal capacity solver
#term 4 week 12 lecture 2

fixedcost = 1.5
target = [0,1,2,4,6,7,8]
cost = [5.4, 5.6, 5.8, 5.7, 5.5, 5.2]
optimaldict = {}



def mincosttogo(currentnum, currentyear, target = target, cost = cost, fixedcost = fixedcost, optimaldict = optimaldict):
    #dynamic!!! programmin!!!
#    print currentyear, currentnum, optimaldict
    if currentyear in optimaldict:
        if currentnum in optimaldict[currentyear]:
            return optimaldict[currentyear][currentnum][1]
        
        
    if currentyear >= len(target): #once we have cleared all objectives
        return 0   
    elif currentnum < target[currentyear]: #if we do not hit the target
        return inf #a thought: should boundary conditions be in the function? why not in the setup?
    else: #calculate your cost to go
        options = []
#        for numtobuildthisyear in range(target[-1]-currentnum+1): 
        for numtobuildthisyear in range(4): #prof selin's formulation has the condition that you can only build 3 power plants in a year.
            costtogoofoption = bool(numtobuildthisyear)*fixedcost + numtobuildthisyear*cost[currentyear] + mincosttogo(currentnum + numtobuildthisyear, currentyear+1)
            #the cost to go for an option is costtogo if you do not build, fixedcost + cost*numtobuild + costtogo if you do
            
            options.append([numtobuildthisyear, costtogoofoption])
        mincosttogoofoption = min(options, key = lambda x: x[1]) #choose the choice that gives the min cost to go
        optimaldict[currentyear][currentnum] = mincosttogoofoption #update optimaldict with the cost to go of that option
    return mincosttogoofoption[1]



    
def optimalcapacityexpansion(fixedcost = fixedcost, target = target, cost = cost, optimaldict = optimaldict):
    totalyears = len(target)
    padding = totalyears - len(cost) #pad cost to be same length as target
    if padding > 0:
        for iteation in range(padding):
            cost.append(inf) #cost of building in target year is inf - you need to build before that year
    #set boundary conditions
    for year in range(totalyears):
        optimaldict[year] = dict.fromkeys(range(target[year]), ["x", inf])
    for num in range(target[year]+1, max(target)):
        optimaldict[totalyears-1][num] = ["x", 0]
    optimalcost = mincosttogo(0,0)
#
#    finaltarget = max(target)
#    current = 0
#    firstpurchase = optimaldict[0][0]
#    current += firstpurchase[0]
#    while current != finaltarget:
#        for year, minimum in enumerate(target):
#            if current < minimum:
#                break
##        print current
#        nextpurchase = optimaldict[year]
#        for n in sorted(nextpurchase.items(), key = lambda x: x[0], reverse = True):
#            if type(n[1][0]) is not str:
#                nextpurchaseqty = n[0]
#                break
#        current += nextpurchaseqty
#        
#tried making it spit out how much to purchase but ugh
                
    
        
optimalcapacityexpansion()
#print mincosttogo(0,0)
#print mincosttogo(0,5)
print mincosttogo(0,0)