import openai
from config import *

def generate_sql_query(prompt):

    query=f'''
    Generate an SQL query for the following request (Remember:Do not return anything else but the query): {prompt} 

    Data summary: Tables Overview
    table1:
    Columns:
    id (INT, Primary Key)
    col1 (VARCHAR(50)): Example - Names like 'Alice', 'Bob'
    col2 (INT): Example - Integer values like 23, 34
    col3 (DATE): Example - Dates like '2022-01-01'
    col4 (BOOLEAN): Example - Boolean values like TRUE, FALSE
    col5 (DECIMAL(10, 2)): Example - Decimal values like 123.45
    col6 (VARCHAR(50)): Example - Text data like 'Data1', 'Data2'
    col7 (INT): Example - Integer values like 1, 2
    col8 (DATE): Example - Dates like '2023-01-01'
    col9 (BOOLEAN): Example - Boolean values like TRUE, FALSE
    col10 (DECIMAL(10, 2)): Example - Decimal values like 543.21
    
    table2:
    Columns:
    id (INT, Primary Key)
    table1_id (INT, Foreign Key referencing table1(id))
    col1 (VARCHAR(50)): Example - Names like 'David', 'Eve'
    col2 (INT): Example - Integer values like 56, 67
    col3 (DATE): Example - Dates like '2022-04-04'
    col4 (BOOLEAN): Example - Boolean values like TRUE, FALSE
    col5 (DECIMAL(10, 2)): Example - Decimal values like 456.78
    col6 (VARCHAR(50)): Example - Text data like 'Data4', 'Data5'
    col7 (INT): Example - Integer values like 4, 5
    col8 (DATE): Example - Dates like '2023-04-04'
    col9 (BOOLEAN): Example - Boolean values like TRUE, FALSE
    col10 (DECIMAL(10, 2)): Example - Decimal values like 876.54

    table3:
    Columns:
    id (INT, Primary Key)
    table2_id (INT, Foreign Key referencing table2(id))
    col1 (VARCHAR(50)): Example - Names like 'George', 'Hannah'
    col2 (INT): Example - Integer values like 89, 90
    col3 (DATE): Example - Dates like '2022-07-07'
    col4 (BOOLEAN): Example - Boolean values like TRUE, FALSE
    col5 (DECIMAL(10, 2)): Example - Decimal values like 789.01
    col6 (VARCHAR(50)): Example - Text data like 'Data7', 'Data8'
    col7 (INT): Example - Integer values like 7, 8
    col8 (DATE): Example - Dates like '2023-07-07'
    col9 (BOOLEAN): Example - Boolean values like TRUE, FALSE
    col10 (DECIMAL(10, 2)): Example - Decimal values like 1209.87
    
    \nSQL query:'''
    
    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=query,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()



if __name__=='__main__':
    prompt = 'from table3 give me all the values in column 3'

    response = generate_sql_query(prompt)
    print(response)