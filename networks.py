# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:23:21 2017

@author: Isaac Ng
"""

# implementation of djikstra's algorithm
import time  #used for time.sleep while developing
import itertools
import copy
import math

inf = 9999
sep = " to "



    
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
    
class Tedge(Edge): #time-limited edge: used for dijkstra when arcs only open after time <timeopen>
    def __init__(self, sourcetarget, cost, timeopen = 0): #timeopen is a time that the arc is opened at
        Edge.__init__(self, sourcetarget, cost)
        self.timeopen = timeopen
   
    
    
    
def edgesfrompositions(nodeloc, nodestr):
#    print nodeloc, nodestr
    #creating adj matrix data struct
    locdict = dict(zip(nodestr, range(len(nodestr))))
    adjmatrix = []
    for sourcenodename, sourcenodeidx in sorted(locdict.iteritems(), key = lambda x: x[1]):
        adjmatrix.append([])
        print sourcenodename, sourcenodeidx
        for targetnodename, targetnodeidx in locdict.iteritems():
            adjmatrix[sourcenodeidx].append([])
    
    #filling in adj matrix
    for sourceidx, source in enumerate(nodestr):
        for targetidx, target in enumerate(nodestr):
            xdist = nodeloc[sourceidx][0] - nodeloc[targetidx][0]
            ydist = nodeloc[sourceidx][1] - nodeloc[targetidx][1]
            netdist = math.sqrt(xdist**2+ydist**2)
            adjmatrix[sourceidx][targetidx] = netdist
    
    #adjacency matrix input
    edges = []
    for source in nodestr:
        for target in nodestr:
            edge = Edge(*["%s %s" %(source, target), adjmatrix[locdict[source]][locdict[target]]])
            edges.append(edge)    
    return edges
    
    
    
        
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
    
    def shortpathneg_iterate(self, numarcs, costs, preceding): #this is the bellman-moore-ford algorithm but... eponyms...
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
        finalcost = costs[len(self.nodes)-2]
#        print finalcost
        for edge in self.edges:
            if finalcost[edge.source] + edge.cost < finalcost[edge.target]:
                print "Graph has negative loop, returning one edge of aforementioned loop"
                return edge
        return finalcost[target], preceding
    
    def salesman_iterate(self, iteration, origin, visited, current, costs):
#        print "\n", iteration, origin, visited, current, costs
        #visited does not include origin or current
        #iteration is zero-indexed
        #first search the costs dict for an answer
        #cost is frozenset, then current node
#        print self.count
        self.count += 1
        coveredallvisited = costs.get(frozenset(visited))
        if coveredallvisited != None:
            DPanswer = coveredallvisited.get(current)
            if DPanswer != None: 
                return DPanswer #should be a list consisting of route and cost
     
        #if we have never encountered this state, calculate its cost
        possibleroutes = []
        iterationprime = iteration - 1
        for edge in self.backstar(current):
            if edge.source in visited:
                visitedprime = visited[:]
                visitedprime.remove(edge.source)
                currentprime = edge.source
                possibleroute, possiblecost = self.salesman_iterate(iterationprime, origin, visitedprime, currentprime, costs)
                possiblecost += edge.cost
                possibleroute = possibleroute[:]
                possibleroute.append(current)
                possibleroutes.append([possibleroute, possiblecost])
        possibleroutes.append([visited,inf])
        bestroute = min(possibleroutes, key = lambda x: x[1])
        costdictkey = frozenset(bestroute[0])
        costdictkey2 = bestroute[0][-1]
        costs[costdictkey] = {costdictkey2: bestroute}
#        print bestroute
        return bestroute
    
    def salesman(self):
        if len(self.edges)>200:
            print "u mad bro"
        origin = self.nodes[0]
        costs = {frozenset([]):{}}
        for node in self.nodes:
            if node != origin:
                costs[frozenset([])][node] = [[node], inf]
        for edge in self.fwdstar(origin):
            costs[frozenset([])][edge.target] = [[edge.target], edge.cost]
            #{frozenset([]): {origin: [[origin], 0]}}
        
        return self.salesman_iterate(len(self.nodes), origin, self.nodes[1:], origin, costs)
    
    
    
    def improvement_iterate(self, currentsol, potentialnode):
        currentpath = currentsol[0]
        if potentialnode in currentsol: 
            print "wat u doin"
            print currentsol, potentialnode
            return currentsol
        fstar = self.fwdstar(potentialnode)
        bstar = self.backstar(potentialnode)
        fstartargets = [edg.target for edg in fstar]
        fstartargets = dict(zip(fstartargets, fstar))
        bstarsources = [edg.source for edg in bstar]
        bstarsources = dict(zip(bstarsources, bstar))
        potentialswaps = []
        
        for edgeidx, edge in enumerate(currentpath):
            if edgeidx < len(currentpath)-1: #NB: <, not <=
                sourceofedgetobreak, targetofedgetobreak = currentpath[edgeidx:edgeidx+2]
                if sourceofedgetobreak in bstarsources and targetofedgetobreak in fstartargets:
                    potentialswaps.append((sourceofedgetobreak, targetofedgetobreak))
        costsofswap = []
        for swap in potentialswaps:
            edgetobreak = filter(lambda x: x.source == swap[0] and x.target == swap[1], self.edges)
            if len(edgetobreak) > 1:
                print "u wot m8", edgetobreak
            addedcost = bstarsources[swap[0]].cost+fstartargets[swap[1]].cost - edgetobreak[0].cost
            costsofswap.append((addedcost, swap))
        bestswap = min(costsofswap, key = lambda x: x[0])
        toreturn = currentpath[:]
        idxtoinsert = toreturn.index(bestswap[1][1])
        toreturn.insert(idxtoinsert, potentialnode)
        return [toreturn, currentsol[1]+bestswap[0]]
    
#    def tsp_improvement(self, startnetwork = None):
#        if startnetwork != None:
#            for nodenotincluded in self.nodes:
#                if nodenotincluded not in startnetwork[0]:
#                    print "a"
#                    startnetwork = self.improvement_iterate(startnetwork, nodenotincluded)
#        return startnetwork
    def tsp_improvement(self, startnetwork = None):
        if startnetwork != None:
            nodesnotincluded = list(frozenset(self.nodes).difference(startnetwork[0]))

            nodesleft = True
            while nodesleft == True:
                nodenotincluded = nodesnotincluded[random.randint(0, len(nodesnotincluded)-1)]
                startnetwork = self.improvement_iterate(startnetwork, nodenotincluded)
                nodesnotincluded.remove(nodenotincluded)
                if len(nodesnotincluded) == 0:
                    nodesleft = False
        return startnetwork
    
    def tsp_improvement_loop(self, startnetwork = None, numattempt = 10):
        options = []
        if startnetwork != None:
            for attempt in range(numattempt):
                options.append(self.tsp_improvement(startnetwork))
        return min(options, key = lambda x: x[1])
            
                          
edgeData = [            ['a b', 4], ['a c', 2], ['a d', 5], \
            ['b a', 4],             ['b c', 1], ['b d', 3], \
            ['c a', 2], ['c b', 1],             ['c d', 2], \
            ['d a', 5], ['d b', 3], ['d c', 2]           ]

nodestr = list("abcd")

edges = [Edge(*[attr for attr in datapoint]) for datapoint in edgeData]
tsphwnetwork = Network(nodestr, edges)
print tsphwnetwork.improvement_iterate([['d', 'b', 'a'], 12], "c")
print tsphwnetwork.tsp_improvement_loop([['d', 'b', 'a'], 12])

nodestr = list("abcd")

edges = [Edge(*[attr for attr in datapoint]) for datapoint in edgeData]
tsphwnetwork = Network(nodestr, edges)
print tsphwnetwork.salesman()
        
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
net = Network(list("sabcdet"), edges)
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
n = Network(list("abcdefgh"), [ab,ac,ad,bc,be,bf,cd,cf,cg,dg,ef,eh,fg,fh,gh])
#note the extra "g" node
print(n.shortpathneg("a", "h"))



#%% TSP test case

#edgeData = [["a b", 2], ["a c", 4], ["b a", 3], ["b c", 4], ["c a", 5], ["c b", 3]]
#edges = [Edge(*[attr for attr in datapoint]) for datapoint in edgeData]
#tspnet = Network(list("abc"), edges)


        

edgeData11 = [["a b", 2], ["a c", 4], ["b a", 3], ["c a", 5], \
            ["c b", 3], ["a d", 117], ["d b", 1], ["b c", 1], \
            ["b d", 1], ["d c", 1], ["d e", 5], ["e f", 2], \
            ["f g", 2], ["g h", 3], ["h i", 4], ["i j", 3], \
            ["j k", 2], ["k c", 1], ["f c", 12], ["a g", 10], \
            ["k d", 6], ["i c", 9], ["j h", 8], ["e k", 8], \
            ["c k", 7]]
            #tsp tour is cabdefghijk 
edgeData = [["a b", 2], ["a c", 4], ["b a", 3], ["c a", 5], \
            ["c b", 3], ["a d", 117], ["d b", 1], ["b c", 1], \
            ["b d", 1], ["d c", 1]]
edges = [Edge(*[attr for attr in datapoint]) for datapoint in edgeData]
for permut in itertools.permutations("abcd"):
    tspnet = Network(list(permut), edges)
    print tspnet.salesman()

edges = [Edge(*[attr for attr in datapoint]) for datapoint in edgeData11]
tspnet = Network(list("abcdefghijk"), edges)
#print tspnet.salesman()
    
#%% TSP homework
routes = []
nodeloc = [[1.1,5.5],[1.3,6.9],[1.3,9.1],[2.0,4.5],[2.3,8.4],\
           [2.4,9.6],[4.7,7.3],[5.3,5.8],[5.5,9.8],[5.7,3.2],\
           [6.0,6.8],[6.6,4.8],[6.7,2.1],[7.3,5.6],[7.9,7.9],\
           [7.9,9.9],[9.3,0.7],[9.3,8],[9.6,4.9],[9.6,9.1]]
nodestr = list("abcdefghijklmnopqrst")
for attempt in range(1):
    initialnetnodes = zip(nodestr, nodeloc)[:]
    random.shuffle(initialnetnodes)
    initialnetnodes = initialnetnodes[0:10]
    initialnetnodeloc = [node[1] for node in initialnetnodes]
    initialnetnodestr = [node[0] for node in initialnetnodes]
    initialnetedges = edgesfrompositions(initialnetnodeloc, initialnetnodestr)
    initialnet = Network(initialnetnodestr, initialnetedges)
    initialans = initialnet.salesman()
    edges = edgesfrompositions(nodeloc, nodestr)
    tsphwnetwork = Network(nodestr, edges)
    newans = tsphwnetwork.tsp_improvement_loop(initialans, 50)
    routes.append(newans)
print routes
print "\n"
print min(routes, key = lambda x: x[1])
#tsphwnetwork.salesman()
#%% TSP homework subproblem
starttime = time.time
nodeloc = [[1.1,5.5],[1.3,6.9],[1.3,9.1],[2.0,4.5],[2.3,8.4],\
           [2.4,9.6],[4.7,7.3],[5.3,5.8],[5.5,9.8],[5.7,3.2]]
nodestr = list("abcdefghij")
edges = edgesfrompositions(nodeloc, nodestr)
tsphwnetwork = Network(nodestr, edges)

starttime = time.time()
print tsphwnetwork.salesman()
endtime = time.time()
print endtime-starttime


print tsphwnetwork.tsp_improvement([['b', 'e', 'c', 'f', 'i', 'g', 'h', 'j', 'd', 'a'], 20.890510666787485])


#%% TSP homework smol qn
edgeData = [            ['a b', 4], ['a c', 2], ['a d', 5], \
            ['b a', 4],             ['b c', 1], ['b d', 3], \
            ['c a', 2], ['c b', 1],             ['c d', 2], \
            ['d a', 5], ['d b', 3], ['d c', 2]           ]

nodestr = list("abd")

edges = [Edge(*[attr for attr in datapoint]) for datapoint in edgeData]
tsphwnetwork = Network(nodestr, edges)
print tsphwnetwork.salesman()
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
        for numtobuildthisyear in range(4): #prof selin's formulation has the condition that you can only build 3 power plants in a year. (the textbook says so too)
            costtogoofoption = bool(numtobuildthisyear)*fixedcost + numtobuildthisyear*cost[currentyear] + mincosttogo(currentnum + numtobuildthisyear, currentyear+1)
            #the cost to go for an option is costtogo if you do not build, fixedcost + cost*numtobuild + costtogo if you do
            
            options.append([numtobuildthisyear, costtogoofoption])
        mincosttogoofoption = min(options, key = lambda x: x[1]) #choose the choice that gives the min cost to go
        optimaldict[currentyear][currentnum] = mincosttogoofoption #update optimaldict with the cost to go of that option
    return mincosttogoofoption[1]

#backtracking when 

    
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
#in the future instead of doing min() or max() an if is better so that the info can be extracted
                
    
        
optimalcapacityexpansion()
#print mincosttogo(0,0)
#print mincosttogo(0,5)
print mincosttogo(0,0)


