#!/usr/bin/python
import heapq

class RouteFinder:
    def __init__(self, origin, destination, systems): #Setup the route finder
        self.mainStart=origin #initialize the main start system 
        self.mainEnd=destination #initialize the main end system
        self.systems = systems #initialize the systems array
        self.currentCalcs = 0 #Stores the current amount of running calculations
    def getSys(self, sysID): #Returns a system object given an id
        return self.systems[sysID]
##    def get_h(self, node, routeType, start="", end=""): #Get the estimated cost of getting to the end system. Different calculations are used depending on what
##        #is currently wanted
##        if(start == ""): #This and the next if cause start and end to default to mainStart and mainEnd if no custom start and end are given
##            start = self.mainStart
##        if(end == ""):
##            end = self.mainEnd
##        if(routeType == "dl"): #If we are using the default route
##            return node.getSysDistance(end) #Then h is calculated by the system module
##        if(routeType == "j"): #If we are using the jumps route
##            route = self.routeCalc("dl", start, end)
##            return len(route)-1 #Get the amount of jumps from the default route calculation
    def getAdj(self, node): #Get the adjacent systems for a given system
        systems = node.getadjSyss()
        return systems
    def updateNode(self, adj, node, routeType, arrayID): #Update a system
        adj.setG(arrayID,node.getG(arrayID)+adj.getSysDistance(node)) #Update the cost of getting to the current system from the start
        adj.setH(arrayID, self.get_h(adj, routeType)) #Update the estimate of getting to the end from the current system
        adj.setParent(arrayID, node) #Set the parent to be the node we came from
        adj.setF(arrayID, adj.getG(arrayID) + adj.getH(arrayID)) #Set the estimated final cost for the system
    def getRoute(self, routeType): #Main get route method. Calls different methods based on what route type we want
        #j for jumps, dl for default lightyear distance, du for au distance
        if( routeType == "j"):
            return self.jumpsRoute()
    def buildRoute(self, node, arrayID, start): #Recursively Builds the route into an array of systems given a node/system
        route = []#initialize the route array
        if node is start: #If the current node is the start node
            route.append(node) #Append it to the array
            return route #Return the array
        else: #Otherwise
            route = self.buildRoute(node.getParent(arrayID), arrayID, start) #Call the method again on the parent node for the current node
            route.append(node) #After that returns append the current node
            return route #And return the route
##    def routeCalc(self, routeType, start="", end="", ):#Default ly distance route finder
##        if(start == ""): #This and the next if cause start and end to default to mainStart and mainEnd if no custom start and end are given
##            start = self.mainStart
##        if(end == ""):
##            end = self.mainEnd
##        arrayID = self.currentCalcs #Array id for A* value storage arrays in the systems
##        self.currentCalcs +=1 #Increases the number of current calculations being run
##        for sysID, sys in self.systems.items(): #Sets up each system to ensure they are clear for the given arrayID
##            sys.setupAstar(arrayID)
##        opened = [] #Sets up the open list
##        heapq.heapify(opened) #Turns the open list into a priority queue
##        closed = set() #Sets up the closed set
##        heapq.heappush(opened, (start.getF(arrayID), start)) #Add the start to the heapq
##        while len(opened): #While there are open nodes
##            #print(opened)
##            f, node = heapq.heappop(opened) #Get the final estimated cost and the node at the front of the queue
##            closed.add(node) #Add that node to the closed list
##            if node is end: #If the node is the end node
##                route = self.buildRoute(node, arrayID, start) #Build the route and return it
##                self.currentCalcs -= 1 #Calc has finished so subtract one from the current calcs
##                return route
##            adj_ids = self.getAdj(node) #Get the adjacent ids for the current node
##            adj_systems = []#initialize the adjacent systems array
##            for sys in adj_ids: #For each adjacent system id
##                adj_systems.append(self.getSys(sys)) #Get the corosponding system object
##            for adj in adj_systems: #For each adjacent system 
##                if adj not in closed: #If the node is not closed
##                    if (adj.getF(arrayID), adj) in opened: #If the node is open
##                        if adj.getG(arrayID) > node.getG(arrayID) + adj.getSysDistance(node): #If current path better than found path
##                            self.updateNode(adj, node, routeType, arrayID) #Update that node with the current node as parent
##                    else: #Otherwise
##                        self.updateNode(adj, node, routeType, arrayID) #Update the node with the current node as parent
##                        heapq.heappush(opened, (adj.getF(arrayID), adj)) #Then push it onto the queue
    def jumpsRoute(self, start="", end=""):
        if(start == ""): #This and the next if cause start and end to default to mainStart and mainEnd if no custom start and end are given
            start = self.mainStart
        if(end == ""):
            end = self.mainEnd
        arrayID = self.currentCalcs
        self.currentCalcs +=1 #Increases the number of current calculations being run
        for sysID, sys in self.systems.items(): #Sets up each system to ensure they are clear for the given arrayID
            sys.setupAstar(arrayID)
        visited, queue = set(), [start]
        while queue:
            sys = queue.pop(0)
            if(sys == end):
                route = self.buildRoute(sys, arrayID, start) #Build the route and return it
                self.currentCalcs -= 1 #Calc has finished so subtract one from the current calcs
                return route
            if sys not in visited:
                visited.add(sys)
                adj_ids = self.getAdj(sys)
                adj_systems = []
                for adjid in adj_ids: #For each adjacent system id
                    adjsys = self.getSys(adjid)
                    if(adjsys not in visited and adjsys not in queue):
                        adjsys.setParent(arrayID, sys)
                        adj_systems.append(adjsys) #Get the corosponding system object
                queue.extend(adj_systems)
        return visited
    
        
    
