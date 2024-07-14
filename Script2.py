import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('social_network.db')
c = conn.cursor()

# SQL query to get married couples
c.execute('''SELECT person1, person2, start_date 
             FROM relationships 
             WHERE relationship_type = 'spouse' ''')

# Fetch all results
married_couples = c.fetchall()

# Convert query results to DataFrame
df = pd.DataFrame(married_couples, columns=['Person 1', 'Person 2', 'Start Date'])

# Generate CSV file
df.to_csv('married_couples.csv', index=False)

# Close connection
conn.close()
