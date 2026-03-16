from flask import Flask, jsonify
import sqlite3

app = Flast(__name__)

def query_db(query,args=()):
    conn = sqlite3.connect("recipe.db")
    cursor =conn.cursor()
    cursor.execute(query,args)
    data = cursor.fetchall()
    
    return data
    conn.close()
    
@app.route("/api/recipes")
def get_recipes():
    
    
@app.route("/api/recipe/search")
def search_recipes():
    