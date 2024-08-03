import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('social_network.db')
c = conn.cursor()

# SQL query to get married couples
query = '''SELECT person1, person2, start_date 
           FROM relationships 
           WHERE relationship_type = 'spouse' '''
print("Executing query: ", query)
c.execute(query)

# Fetch all results
married_couples = c.fetchall()
print("Number of married couples found:", len(married_couples))

# Check if any data is returned
if married_couples:
    # Convert query results to DataFrame
    df = pd.DataFrame(married_couples, columns=['Person 1', 'Person 2', 'Start Date'])
    
    # Generate CSV file
    csv_file = 'married_couples.csv'
    df.to_csv(csv_file, index=False)
    print(f"CSV file '{csv_file}' has been created.")
else:
    print("No married couples found with the relationship type 'spouse'.")

# Close connection
conn.close()
