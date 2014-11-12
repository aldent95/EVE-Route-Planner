#!/usr/bin/python


class System:
    __exits = [];
    __gatePos = {};
    __sysID;
    __name;
    __constellation;
    __region;
    def __int__(self, sysID, name, constellation, region):
        self.sysID = __sysID;
        self.name = __name;
        self.constellation = __constellation;
        self.region = __region;
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
