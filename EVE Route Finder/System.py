#!/usr/bin/python


class System:
    
    def __init__(self, name, constellation, region, sysID, x, y, z, security):
        self.__sysID = sysID;
        self.__name = name;
        self.__constellation = constellation;
        self.__region = region;
        self.__pos = [x,y,z];
        self.__secutiry = security;
    def addExit(self, exit):
        self.__exits.append(exit);
    def addGatePos(self, gate, pos):
        self.__gatePos[gate] = pos;
    def getExit(self, exitid):
        for exit in self.__exits:
            if exit.getID() == exitid:
                return exit;
        return;
    def getGatePos(self, gateID):
        return self.__gatePos[gateID];
    def getExits(self):
        return self.__exits;
    def getID(self):
        return self.__sysID;
    def getName(self):
        return self.__name;
    def getConstellation(self):
        return self.__constellation;
    def getRegion(self):
        return self.__region;
    def toString(self):
        tempstr = self.__name + " " + self.__region;
        return tempstr;
