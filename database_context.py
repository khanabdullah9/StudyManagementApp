import mysql.connector as db

class Context:
    def __init__(self):
        try:
            self.mydb =  db.connect(
            host = "localhost",
            username = "root",
            password = "Abscular09@",
            database = "StudyManagementApplication"
            )   
        except Exception as e:
            print("Connection with database could not be made.")

    def test_db_connection(self):
        print(self.mydb)
    
    
    
    def run_sql(self,query):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(query)
        except Exception as e:
            print("[ERROR] "+e)
            
    def run_sql_get_data(self,query):
        try:
            cursor = self.mydb.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("[ERROR] "+e)
