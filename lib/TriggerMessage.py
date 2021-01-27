import constants

class TriggerMessage():
    
    __fileArray__ = []

    __summonArray__ = []
    __matchArray__ = []

    def __init__(self): 
        # load trigger messages from the file
        self.__loadFile__()

    def __loadFile__(self):
        f = open(constants.TRIGGERS_PATH, "r")

        self.__fileArray__ = f.read().splitlines()
        
        lastIdentifier = 0
        for elem in self.__fileArray__:
            if (elem[0] == "="):
                lastIdentifier = int(elem.split("=")[1])
                continue
            
            if (lastIdentifier == constants.TRIGGER_TYPE_PING):
                self.__summonArray__.append(elem)
                continue

            if (lastIdentifier == constants.TRIGGER_TYPE_MATCH):
                self.__matchArray__.append(elem)
                continue

        f.close()

    def checkTrigger(self, msgContent, triggerType=constants.TRIGGER_TYPE_PING):
        msgArray = msgContent.split(" ")
    
        if (triggerType == constants.TRIGGER_TYPE_PING): 
            return self.__summon__(msgArray)
        
        if (triggerType == constants.TRIGGER_TYPE_MATCH):
            return self.__match__(msgArray)

    def __summon__(self, arr):
        for elem in self.__summonArray__:
            if (elem in arr): return True
        return False
    
    def __match__(self, arr):
        for elem in self.__matchArray__:
            if (elem in arr): return True
        return False
