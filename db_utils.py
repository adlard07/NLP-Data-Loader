from gpt_utils import generate_sql_query
from mysql import connector
import pandas as pd
from config import *

def execute_query(query):
    host = "localhost"
    user = "home"
    password = "Adelard@1234"
    database = "myWorkDatabase"
    result = {}
    try:
        connection = connector.connect(
            host = host,
            user = user,
            password = password,
            database = database
            )
        use_query = "USE myWorkDatabase;"
        cursor = connection.cursor()

        cursor.execute(use_query)
        connection.commit()

        cursor.execute(query)
        response = cursor.fetchall()

        for i, resp in enumerate(response):
            result[i] = resp
            
        return result

    except Exception as e:
        return str(e)
    
if __name__=="__main__":
    prompt = 'from table3 give me all the values in column 3 and column 4'

    query = generate_sql_query(prompt)
    print(query)
    result = execute_query(query)
    df = df = pd.DataFrame.from_dict(result, orient='index')
    print(df)