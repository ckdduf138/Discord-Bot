import myDataBase as db

# SQL Query Class
class Query:

    # INSERT ToDoList
    def InsertToDoList(values):
        query = "INSERT INTO ToDoList VALUES(?,?,?,?)"

        db.ExecuteQuery(query,values)