from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)


def query_db(query, args=()):
    conn = sqlite3.connect("recipes.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rows = cursor.fetchall()
    results = [dict(row) for row in rows]
    conn.close()
    return results

#API endpoint 1
@app.route("/api/recipes")
def get_recipes():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))
    offset = (page - 1) * limit
    data = query_db("SELECT * FROM recipes ORDER BY rating DESC LIMIT ? OFFSET ?", (limit, offset))
    return jsonify({
        "page": page, 
        "limit": limit,
        "total": len(data), # page,limit,total values are returned at the end of response in the browser
        "data": data
    })

#API endpoint 2
@app.route("/api/recipes/search")
def search_recipes():
    calories = request.args.get("calories")
    title = request.args.get("title")
    cuisine = request.args.get("cuisine")
    total_time = request.args.get("total_time")
    rating = request.args.get("rating")
    data = query_db(
        """SELECT * FROM recipes WHERE (json_extract(nutrients, '$.calories') = ? OR ? IS NULL) 
        AND (title = ? OR ? IS NULL)
        AND (cuisine = ? OR ? IS NULL)
        AND (total_time = ? OR ? IS NULL)
        AND (rating = ? OR ? IS NULL);""",
        (calories, calories, title, title, cuisine, cuisine, total_time, total_time, rating, rating))
    
    return jsonify({
        "data": data
    })


if __name__ == "__main__":
    app.run(debug=True)