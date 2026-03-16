from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_db(query,args=()):
    conn = sqlite3.connect("recipes.db")
    cursor =conn.cursor()
    cursor.execute(query,args)
    data = cursor.fetchall()
    
    return data
    conn.close()
    
@app.route("/api/recipes")
def get_recipes():
    page = request.args.get("page")
    limit = request.args.get("limit")
    data = query_db("SELECT * FROM recipes ORDER BY rating DESC limit ?", (limit,))
    return jsonify(data)



@app.route("/api/recipes/search")
def search_recipes():
    calories = request.args.get("calories")
    title = request.args.get("title")
    cuisine = request.args.get("cuisine")
    total_time = request.args.get("total_time")
    rating = request.args.get("rating")
    
    data = query_db("SELECT * FROM recipes WHERE json_extract(nutrients, '$.calories') = ? OR title = ? OR cuisine = ? OR total_time = ? OR rating = ?", (calories, title, cuisine, total_time, rating))

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)