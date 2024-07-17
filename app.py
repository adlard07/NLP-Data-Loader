from flask import Flask, request, render_template, jsonify
from gpt_utils import generate_sql_query
from db_utils import execute_query

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate_query', methods=['POST'])
def generate_query():
    prompt = request.json['prompt']
    sql_query = generate_sql_query(prompt)
    result = execute_query(sql_query)

    return jsonify({
        'query': sql_query, 
        'result': result
        })



if __name__ == '__main__':
    app.run(debug=True, port=2024)
