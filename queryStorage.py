import myDataBase as db

# SQL Query Class
class Query:

    # INSERT ToDoList
    def InsertToDoList(values):
        query = '''
            INSERT INTO ToDoList(
            [ID],
            [CONTENT],
            [STATUS],
            [INDATE])
            VALUES(?,?,?,?)
            '''

        db.ExecuteQuery(query,values)