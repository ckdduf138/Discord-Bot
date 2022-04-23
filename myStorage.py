#User Storage
import numpy as np

userList = [["test1","test1"]]   

def ListInUser(userid):
    exitFlag = False
    for idx in range(len(userList)):    
        if userList[idx][0] == userid:
            return idx
    if exitFlag == False:
        return 0

def add(userId, userMsg):
    idx = ListInUser(userId)
    if len(userMsg) >= 5:
        userMsg = userMsg[5:]
        if idx:
            userList[idx].append(userMsg)
        else:
            userList.append([userId,userMsg])
    else:
        return

def listDelete(userId, userMsg):
    idx = ListInUser(userId)
    userList[idx].remove(userMsg)
        
def getList(userId):
    idx = ListInUser(userId)
    if idx:
        return userList[idx]
    else:
        return "0"
