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
def parse_operator(value):
    if value.startswith(">="):
        return ">=", value[2:]
    if value.startswith("<="):
        return "<=", value[2:]
    if value.startswith(">"):
        return ">", value[1:]
    if value.startswith("<"):
        return "<", value[1:]
    if value.startswith("="):
        return "=", value[1:]
    return "=", value


@app.route("/api/recipes/search")
def search_recipes():

    calories = request.args.get("calories")
    title = request.args.get("title")
    cuisine = request.args.get("cuisine")
    total_time = request.args.get("total_time")
    rating = request.args.get("rating")

    query = "SELECT * FROM recipes"
    conditions = []
    params = []

    if calories:
        op, val = parse_operator(calories)
        conditions.append("json_extract(nutrients, '$.calories') " + op + " ?")
        params.append(val)

    if title:
        conditions.append("title LIKE ?")
        params.append("%" + title + "%")

    if cuisine:
        conditions.append("cuisine = ?")
        params.append(cuisine)

    if total_time:
        op, val = parse_operator(total_time)
        conditions.append("total_time " + op + " ?")
        params.append(val)

    if rating:
        op, val = parse_operator(rating)
        conditions.append("rating " + op + " ?")
        params.append(val)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    data = query_db(query, params)

    return jsonify({
        "data": data
    })

if __name__ == "__main__":
    app.run(debug=True)