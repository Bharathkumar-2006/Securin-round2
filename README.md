#Recipe Data Collection 
The project focuses on collecting the US recipe data from a json file and stores it in a sqlite3 database so that it can be retrieved using an API call from the browser.
To download this repository , use the following command in your terminal.
git clone https://github.com/Bharathkumar-2006/Securin-round2
To run this project, Follow the steps correctly:
####1.Download the necessary packages from requirements.txt 
pip install -r requirements.txt
####2.Run the database.py file 
python database.py
This command will parse the json file and load the json objects into dataframes using pandas. Then the pandas will import those dataframes into sqlite3 database
Now you have successfully loaded the json objects into sqlite3 database. I have choosed the sqlite3 database because it is lightweight, serverless and lives in memory. There is no need for extra servers or applications to install. It is widely used in microservices , mobile apps and more.
####3.Run the app.py file
python app.py
This runs the flask app and open a port 5000 on your computer. You can visit the url http://127.0.0.1:5000 to access the application.
####API Documentation
There are two API endpoints in this project. They are 
1. API Endpoint 1: Get All Recipes (Paginated and Sorted by Rating)
URL: /api/recipes
Method: GET
Query Parameters:
page: Page number for pagination (default is 1).
limit: Number of recipes per page (default is 10).
Response: A list of recipes sorted by rating in descending order.
Example request:
GET /api/recipes?page=1&limit=10
2. API Endpoint 2: Search Recipes
URL: /api/recipes/search
Method: GET
Query Parameters:
calories: Filter by calories (greater than, less than, or equal to a
specific value).
title: Search by recipe title (partial match).
cuisine: Filter by cuisine.
total_time: Filter by total time (greater than, less than, or equal to a
specific value).
rating: Filter by rating (greater than, less than, or equal to a specific
value).
Example request:
GET /api/recipes/search?calories =<= 400&title=pie&rating=>=4.5

You can view the responses by visiting the respective urls in your browser.