from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def query_db(query,args=()):
    conn = sqlite3.connect("recipe.db")
    cursor =conn.cursor()
    cursor.execute(query,args)
    data = cursor.fetchall()
    
    return data
    conn.close()
    
@app.route("/api/recipes")
def get_recipes():
    #with query parameters page and limit
    page = request.args.get("page")
    limit = request.args.get("limit")
    data = query_db("SELECT * FROM recipes limit ? ORDER BY rating DESC", (limit,))
    return jsonify(data)



@app.route("/api/recipe/search")
def search_recipes():
    calories = request.args.get("calories")
    title = request.args.get("title")
    cuisine = request.args.get("cuisine")
    total_time = request.args.get("total_time")
    rating = request.args.get("rating")
    
    data = query_db("SELECT * FROM recipes WHERE calories = ? AND title = ? AND cuisine = ? AND total_time = ? AND rating = ?", (calories, title, cuisine, total_time, rating))

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)