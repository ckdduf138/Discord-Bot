#User Storage

from datetime import datetime
import queryStorage as qs

userList = [["test1","test1"]]   

def ListInUser(userid):
    exitFlag = False
    for idx in range(len(userList)):    
        if userList[idx][0] == userid:
            return idx
    if exitFlag == False:
        return 0

def addList(userId, userMsg):
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        values = (str(userId), userMsg, "000", now)
        qs.Query.InsertToDoList(values)

def listDelete(userId, userMsg):
    idx = ListInUser(userId)
    userList[idx].remove(userMsg)
        
def getList(userId):
    idx = ListInUser(userId)
    if idx:
        return userList[idx]
    else:
        return "0"
