import myDataBase as db

# SQL Query Class
class Query:

    # SELECT ToDoList
    def SelectToDoList(values):
        query = '''
            SELECT
            [CONTENT],
            [STATUS]
            FROM ToDoList
            WHERE 1=1
            AND [ID] = ?
            '''

        return db.ExecuteQuery(query,values)

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

    def DeleteToDoList(values):
        query = '''
        DELETE FROM ToDoList
        WHERE 1=1
        AND [ID] = ?
        AND [CONTENT] = ?
        '''

        db.ExecuteQuery(query, values)

    def UpdateToDoList(values):
        query = '''
        UPDATE ToDoList
        SET [STATUS] = '001'
        WHERE 1=1
        AND [ID] = ?
        AND [CONTENT] = ?
        '''

        db.ExecuteQuery(query, values)