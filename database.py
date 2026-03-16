import pandas as pd
import sqlite3
import json

df = pd.read_json('US_recipes_null.json', orient='index')

cols = ['cuisine', 'title', 'rating', 'prep_time', 'cook_time', 'total_time', 'description', 'nutrients', 'serves']
df = df[cols]

df['nutrients'] = df['nutrients'].apply(json.dumps)

conn = sqlite3.connect('recipes.db')
df.to_sql('recipes', conn, if_exists='replace', index=False)
conn.close()
