import sqlite3

def ExecuteQuery(query,value):
    # 연결
    conn = sqlite3.connect("ToDo.db", isolation_level=None)
    # 커서 획득
    c = conn.cursor()
    # SQL문 실행
    c.execute(query,value)

    return