#!/usr/bin/python
from GeneralError import GeneralError
import math  
class System:
    
    def build(self, name, constellation, region, sysID, x, y, z, security):
        self.__sysID = sysID;
        self.__name = name;
        self.__constellation = constellation;
        self.__region = region;
        x = convert(x,1);
        y = convert(y,1);
        z = convert(z,1);
        self.__pos = [x,y,z];
        self.__security = round(float(security),1);
        self.__adjSyss = [];
        self.__gatePos = {};
        self.parent = []
        return(self)
    def addadjSys(self, adjSys):
        if isinstance(adjSys, System):
            self.__adjSyss.append(adjSys)
        else:
            raise TypeError("Trying to add something that is not a system to adjacent systems")
    def setParent(self, num, entry):
        if not isinstance(num, int):
            raise TypeError("Did not pass type int as num argument")
        if not isinstance(entry, System):
            raise TypeError("Did not pass type system as the parent")
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
        foundSys = ""
        if len(self.__adjSyss) == 0:
            raise IndexError("System does not have any adjacent systems")
        for adjSys in self.__adjSyss:
            if adjSys.getID() == adjSysid:
                foundSys = adjSys;
        if  not isinstance(foundSys, System):
            raise ValueError("No adjacent system found with given id")
        return foundSys
    def getGatePos(self, adjSysId):
        return self.__gatePos[adjSysId]
    def getSecurity(self):
        return self.__security
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
        if gate1 == gate2:
            raise GeneralError(5, "Gate 1 and 2 are the same")
        pos1 = self.__gatePos[gate1];
        pos2 = self.__gatePos[gate2];
        x = pow((float(pos2[0])-float(pos1[0])),2);
        y = pow((float(pos2[1])-float(pos1[1])),2);
        z = pow((float(pos2[2])-float(pos1[2])),2);
        distance = (math.sqrt(x+y+z))/1000;
        distance = round(distance/149597871,1);
        return distance;
    def getSysDistance(self, other):
        if not isinstance(other, System):
            raise TypeError("Cannot get distance when not passed a second system object")
        pos1 = self.getPOS();
        pos2 = other.getPOS();
        x = pow((float(pos2[0])-float(pos1[0])),2);
        y = pow((float(pos2[1])-float(pos1[1])),2);
        z = pow((float(pos2[2])-float(pos1[2])),2);
        distance = (math.sqrt(x+y+z))/1000;
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
