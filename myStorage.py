#User Storage

import datetime
import queryStorage as qs

userList = [["test1","test1"]]   

def ListInUser(userid):
    exitFlag = False
    for idx in range(len(userList)):    
        if userList[idx][0] == userid:
            return idx
    if exitFlag == False:
        return 0

def add(userId, userMsg):

        now = datetime.datetime.now()

        values = (userId, userMsg, 0, now)
        qs.Query.Insert(values)
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
