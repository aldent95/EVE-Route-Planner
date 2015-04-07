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
        self.__adjSyss = [];
        self.__gatePos = {};
        self.g = []
        self.h = []
        self.f = []
        self.parent = []
    def getG(self, num):
        return self.g[num]
    def getH(self, num):
        return self.h[num]
    def getF(self, num):
        return self.f[num]
    def getParent(self, num):
        return self.parent[num]
    def setG(self, num, entry):
        self.g[num] = entry
    def setH(self, num, entry):
        self.h[num] = entry
    def setF(self, num, entry):
        self.f[num] = entry
    def setParent(self, num, entry):
        self.parent[num] = entry
    def setupAstar(self, arrayID):
        if len(self.g) <= arrayID:
            while len(self.g) <= arrayID:
                self.g.append(0)
                self.h.append(0)
                self.f.append(0)
                self.parent.append("")
        else:
            self.g[arrayID] = 0
            self.h[arrayID] = 0
            self.f[arrayID] = 0
            self.parent[arrayID] = ""
    def addadjSys(self, adjSys):
        self.__adjSyss.append(adjSys);
    def addGatePos(self, gate, pos):
        pos[0] = convert(pos[0],2);
        pos[1] = convert(pos[1],2);
        pos[2] = convert(pos[2],2);
        self.__gatePos[gate] = pos;
    def getadjSys(self, adjSysid):
        for adjSys in self.__adjSyss:
            if adjSys.getID() == adjSysid:
                return adjSys;
        return;
    def getGatePos(self, gateID):
        return self.__gatePos[gateID];
    def getadjSyss(self):
        return self.__adjSyss;
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
    def getSysDistance(self, other):
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
