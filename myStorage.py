#User Storage

from datetime import datetime
import queryStorage as qs

def AddList(userId, userMsg):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    values = (str(userId), userMsg, "000", now)
    qs.Query.InsertToDoList(values)

def DeleteList(userId, userMsg):
    values = (str(userId), userMsg)
    qs.Query.DeleteToDoList(values)
        
def UpdateList(userId, userMsg):
    values = (str(userId), userMsg)
    qs.Query.UpdateToDoList(values)

def SelectList(userId):
    values = (userId,)
    return qs.Query.SelectToDoList(values)
