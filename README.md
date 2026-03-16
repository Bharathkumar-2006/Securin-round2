# Recipe Data Collection 
## Project Overview

The project focuses on collecting US recipe data from a JSON file and storing it in a SQLite3 database, enabling retrieval via API calls from the browser.

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Bharathkumar-2006/Securin-round2
```

### 1. Install Dependencies

Download the necessary packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Load Data into Database

Run the `database.py` file:

```bash
python database.py
```

This command parses the JSON file, loads the objects into dataframes using pandas, and imports them into the SQLite3 database.\
The SQLite3 DB will have the table name as "recipes" and have the following columns 'id',cuisine', 'title', 'rating', 'prep_time', 'cook_time', 'total_time', 'description', 'nutrients', 'serves'.\
SQLite3 is chosen for its lightweight, serverless, and in-memory nature. No extra servers or applications are required. It is widely used in microservices, mobile apps, and more.

### 3. Start the Application

Run the `app.py` file:

```bash
python app.py
```

This launches the Flask app and opens port 5000. Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the application.

---

## API Documentation

### 1. Get All Recipes (Paginated and Sorted by Rating)

- **URL:** `/api/recipes`
- **Method:** `GET`
- **Query Parameters:**
    - `page`: Page number for pagination (default is 1)
    - `limit`: Number of recipes per page (default is 10)
- **Response:** List of recipes sorted by rating (descending)

**Example Request:**

```
GET /api/recipes?page=1&limit=10
```

---

### 2. Search Recipes

- **URL:** `/api/recipes/search`
- **Method:** `GET`
- **Query Parameters:**
    - `calories`: Filter by calories (greater than, less than, or equal to a specific value)
    - `title`: Search by recipe title (partial match)
    - `cuisine`: Filter by cuisine
    - `total_time`: Filter by total time (greater than, less than, or equal to a specific value)
    - `rating`: Filter by rating (greater than, less than, or equal to a specific value)

**Example Request:**

```
GET /api/recipes/search?calories=<=400&title=pie&rating=>=4.5
```

---

You can view the responses by visiting the respective URLs in your browser.