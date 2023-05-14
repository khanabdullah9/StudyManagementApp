import mysql.connector as db


class Context:
    def __init__(self):
        try:
            self.mydb = db.connect(
                host="localhost",
                username="root",
                password="Abscular09@",
                database="StudyManagementApplication"
            )
        except Exception as e:
            print("Connection with database could not be made.")
            print("[ERROR] " + e.__str__())

    def test_db_connection(self):
        print(self.mydb)

    def run_sql(self, query):
        """
        Run sql query
        @param query: query
        @return: None
        """
        try:
            cursor = self.mydb.cursor()
            cursor.execute(query)
        except Exception as e:
            print("[ERROR] " + e.__str__())

    def run_sql_get_data(self, query):
        """
        Run sql query
        @param query: query
        @return: data
        """
        try:
            cursor = self.mydb.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Exception as e:
            print("[ERROR] " + e.__str__())

    def run_procedure(self, proc_name, proc_params):
        """
        Run stored procedure
        @param proc_name: str: Name of procedure
        @param proc_params: list: List of procedures
        @return: data
        """
        param_str = ""
        if len(proc_params) > 0:
            param_str = self.create_param_str(proc_params)
        query = f"CALL {proc_name}({param_str});"
        result = self.run_sql_get_data(query)
        return result

    def create_param_str(self, proc_params):
        """
        Create a string of parameters that goes in side the '()' or stored procedure
        @param proc_params: list: parameters
        @return: string of parameters
        """
        param_str = ""
        for p in range(0, len(proc_params) - 1):
            param_str += f"'{proc_params[p]}',"

        p1 = proc_params[len(proc_params) - 1]
        index_p1 = proc_params.index(p1)
        param_str += f"'{proc_params[index_p1]}'"

        return param_str
