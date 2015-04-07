#!/usr/bin/python
import heapq

class RouteFinder:
    def __init__(self, origin, destination, systems): #Setup the route finder
        self.mainStart=origin #initialize the main start system 
        self.mainEnd=destination #initialize the main end system
        self.opened = [] #initialize the opened array
        heapq.heapify(self.opened) #Set the opened array to be a heap queue
        self.closed=set() #initialize the closed set
        self.systems = systems #initialize the systems array
    def getSys(self, sysID): #Returns a system object given an id
        return self.systems[sysID]
    def get_h(self, node, routeType, start="", end=""): #Get the estimated cost of getting to the end system. Different calculations are used depending on what
        #is currently wanted
        if(start == ""):
            start = self.mainStart
        if(end == ""):
            end = self.mainEnd
        if(routeType == "dl"): #If we are using the default route
            return node.getSysDistance(end) #Then h is calculated by the system module
        if(routeType == "j"): #If we are using the jumps route
            print(start.getName() + "\t" + end.getName())
            route = self.lyDistanceRoute(start, end)
            print(type(route))
            return len(route)-1 #Get the amount of jumps from the default route calculation
    def getAdj(self, node): #Get the adjacent systems for a given system
        systems = node.getadjSyss()
        return systems
    def updateNode(self, adj, node, routeType): #Update a system
        adj.g = node.g+adj.getSysDistance(node) #Update the cost of getting to the current system from the start
        adj.h = self.get_h(adj, routeType) #Update the estimate of getting to the end from the current system
        adj.parent = node #Set the parent to be the node we came from
        adj.f = adj.h + adj.g #Set the estimated final cost for the system
    def getRoute(self, routeType): #Main get route method. Calls different methods based on what route type we want
        #j for jumps, dl for default lightyear distance, du for au distance
        if(routeType == "j"):
            return self.jumpsRoute()
        if(routeType == "dl"):
            route =  self.lyDistanceRoute()
            #print(type(route))
            #for sys in route:
            #    print(sys.getName())
            #    print(type(sys))
            #    print(self.get_h(sys, "j", sys))
            return route
        if(routeType == "du"):
            return self.auDistanceRoute()
    def buildRoute(self, node): #Recursively Builds the route into an array of systems given a node/system
        route = []#initialize the route array
        if node is self.mainStart: #If the current node is the start node
            route.append(node) #Append it to the array
            return route #Return the array
        else: #Otherwise
            route = self.buildRoute(node.parent) #Call the method again on the parent node for the current node
            route.append(node) #After that returns append the current node
            return route #And return the route
    def lyDistanceRoute(self, start="", end=""):#Default ly distance route finder
        if(start == ""):
            start = self.mainStart
        if(end == ""):
            end = self.mainEnd
        opened = []
        heapq.heapify(opened)
        closed = set()
        print(start.getName() + " " + end.getName())
        heapq.heappush(opened, (start.f, start)) #Add the start to the heapq
        while len(opened): #While there are open nodes
            f, node = heapq.heappop(opened) #Get the final estimated cost and the node at the front of the queue
            closed.add(node) #Add that node to the closed list
            if node is end: #If the node is the end node
                print("Building route")
                return self.buildRoute(node) #Build the route and return it
            adj_ids = self.getAdj(node) #Get the adjacent ids for the current node
            adj_systems = []#initialize the adjacent systems array
            for sys in adj_ids: #For each adjacent system id
                adj_systems.append(self.getSys(sys)) #Get the corosponding system object
            for adj in adj_systems: #For each adjacent system 
                if adj not in closed: #If the node is not closed
                    if (adj.f, adj) in opened: #If the node is open
                        if adj.g > node.g + adj.getSysDistance(node): #If current path better than found path
                            self.updateNode(adj, node, "dl") #Update that node with the current node as parent
                    else: #Otherwise
                        self.updateNode(adj, node, "dl") #Update the node with the current node as parent
                        heapq.heappush(opened, (adj.f, adj)) #Then push it onto the queue
    def jumpsRoute(self):
        return
    def auDistanceRoute(self):
        return
    
        
    
