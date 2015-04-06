#!/usr/bin/python
import heapq

class RouteFinder:
    def __init__(self, origin, destination, systems):
        self.start=origin
        self.end=destination
        self.opened = []
        heapq.heapify(self.opened)
        self.closed=set()
        self.systems = systems
    def getSys(self, sysID):
        return self.systems[sysID]
    def get_h(self, node):
        return node.getSysDistance(self.end)
    def getAdj(self, node):
        systems = node.getadjSyss()
        return systems
    def updateNode(self, adj, node):
        adj.g = node.g+adj.getSysDistance(node)
        adj.h = self.get_h(adj)
        adj.parent = node
        adj.f = adj.h + adj.g
    def getRoute(self, routeType): #j for jumps, dl for default lightyear distance, du for au distance
        if(routeType == "j"):
            return self.jumpsRoute()
        if(routeType == "dl"):
            return self.lyDistanceRoute()
        if(routeType == "du"):
            return self.auDistanceRoute()
    def buildRoute(self, node):
        route = []
        if node is self.start:
            route.append(node)
            return route
        else:
            route = self.buildRoute(node.parent)
            route.append(node)
            return route
    def lyDistanceRoute(self):
         heapq.heappush(self.opened, (self.start.f, self.start))
         while len(self.opened):
             f, node = heapq.heappop(self.opened)
             self.closed.add(node)
             if node is self.end:
                 return self.buildRoute(node)
             adj_ids = self.getAdj(node)
             adj_systems = []
             for sys in adj_ids:
                 adj_systems.append(self.getSys(sys))
             for adj in adj_systems:
                 if adj not in self.closed:
                     if (adj.f, adj) in self.opened:
                         if adj.g > node.g + adj.getSysDistance(node):
                             self.updateNode(adj, node)
                     else:
                         self.updateNode(adj, node)
                         heapq.heappush(self.opened, (adj.f, adj))
    def jumpsRoute(self):
        return
    def auDistanceRoute(self):
        return
    
        
    
