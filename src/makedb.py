import mysql.connector
import os
def execute_sql_file(filename, db_connection):
    with open(filename, "r") as sql_file:
        queries = sql_file.read().split(";")
        
        # iterate through each query in the list of queries
        for query in queries:
            if query.strip() != "":
                # check if the current query is a trigger definition
                if "CREATE TRIGGER" in query:
                    # set the delimiter to something else to avoid conflicts with semicolons in the trigger definition
                    db_connection.cursor().execute("DELIMITER $$")
                    
                    # execute the trigger definition
                    db_connection.cursor().execute(query)
                    
                    # reset the delimiter back to semicolon
                    db_connection.cursor().execute("DELIMITER ;")
                else:
                    # execute the query as is
                    db_connection.cursor().execute(query)
                
                # commit the changes to the database
                db_connection.commit()

def main():
    # create database connection
    db_connection = mysql.connector.connect(
        host="localhost",
        user=os.environ['USER'],
        password=os.environ['PASS'],
    )
    
    # execute SQL file
    execute_sql_file("intialize.sql", db_connection)
    
    # close database connection
    db_connection.close()

if __name__ == "__main__":
    main()
