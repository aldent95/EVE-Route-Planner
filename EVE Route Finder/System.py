#!/usr/bin/python

import math  
class System:
    
    def build(self, name, constellation, region, sysID, x, y, z, security):
        try:
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
            self.parent = []
            return(self)
        except ValueError:
            return [3, "Error, System file data corrupt, error passed to GUI"]
    def addadjSys(self, adjSys):
        self.__adjSyss.append(adjSys)
    def setParent(self, num, entry):
        while len(self.parent) <= num:
            self.parent.append("")
        self.parent[num] = entry
    def getParent(self, num):
        return self.parent[num]
    def addGatePos(self, gate, pos):
        pos[0] = convert(pos[0],2)
        pos[1] = convert(pos[1],2)
        pos[2] = convert(pos[2],2)
        self.__gatePos[gate] = pos
    def getadjSys(self, adjSysid):
        for adjSys in self.__adjSyss:
            if adjSys.getID() == adjSysid:
                return adjSys;
        return;
    def getGatePos(self, adjSysId):
        return self.__gatePos[adjSysId];
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
        x = pow((float(pos2[0])-float(pos1[0])),2);
        y = pow((float(pos2[1])-float(pos1[1])),2);
        z = pow((float(pos2[2])-float(pos1[2])),2);
        distance = (sqrt(x+y+z))/1000;
        distance = round(distance/149597871,1);
        return distance;
    def getSysDistance(self, other):
        pos1 = self.getPOS();
        pos2 = other.getPOS();
        x = pow((float(pos2[0])-float(pos1[0])),2);
        y = pow((float(pos2[1])-float(pos1[1])),2);
        z = pow((float(pos2[2])-float(pos1[2])),2);
        distance = (sqrt(x+y+z))/1000;
        return distance;
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __hash__(self):
        return hash(self.__sysID)



def convert(num,conType):
    if(conType == 1):
        num = num.split('e+');
    else:
        num = num.split('E');
    num[0] = float(num[0]);
    if len(num) >1:
        num[1] = float(num[1]);
        num = num[0]*pow(10,num[1]);
    else:
        num = num[0];
    return num;
