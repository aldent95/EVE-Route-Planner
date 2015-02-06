#!/usr/bin/python
import math

class System:
    
    def __init__(self, name, constellation, region, sysID, x, y, z, security):
        self.__sysID = sysID;
        self.__name = name;
        self.__constellation = constellation;
        self.__region = region;
        x = convert(x,1);
        y = convert(y,1);
        z = convert(z,1);
        self.__pos = [x,y,z];
        self.__secutiry = security;
        self.__exits = [];
        self.__gatePos = {};
    def addExit(self, exit):
        self.__exits.append(exit);
    def addGatePos(self, gate, pos):
        pos[0] = convert(pos[0],2);
        pos[1] = convert(pos[1],2);
        pos[2] = convert(pos[2],2);
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
    def getPOS(self):
        return self.__pos
    def getGateDistance(self, gate1, gate2):
        pos1 = self.__gatePos[gate1];
        pos2 = self.__gatePos[gate2];
        x = math.pow((float(pos2[0])-float(pos1[0])),2);
        y = math.pow((float(pos2[1])-float(pos1[1])),2);
        z = math.pow((float(pos2[2])-float(pos1[2])),2);
        distance = (math.sqrt(x+y+z))/1000;
        distance = round(distance/149597871,1);
        return distance;
    def getSysDistnace(self, other):
        pos1 = self.getPOS();
        pos2 = other.getPOS();
        x = math.pow((float(pos2[0])-float(pos1[0])),2);
        y = math.pow((float(pos2[1])-float(pos1[1])),2);
        z = math.pow((float(pos2[2])-float(pos1[2])),2);
        distance = (math.sqrt(x+y+z))/1000;
        return distance;
def convert(num,conType):
    if(conType == 1):
        num = num.split('e+');
    else:
        num = num.split('E');
    num[0] = float(num[0]);
    if len(num) >1:
        num[1] = float(num[1]);
        num = num[0]*math.pow(10,num[1]);
    else:
        num = num[0];
    return num;
