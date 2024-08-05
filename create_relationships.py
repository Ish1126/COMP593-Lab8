"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from faker import Faker
import random

# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS relationships (
        id INTEGER PRIMARY KEY,
        person1_id INTEGER NOT NULL,
        person2_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        start_date TEXT NOT NULL,
        FOREIGN KEY (person1_id) REFERENCES people(id),
        FOREIGN KEY (person2_id) REFERENCES people(id)
    );
    """
    cur.execute(create_table_query)
    con.commit()
    con.close()

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    fake = Faker()
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    # Fetch all person IDs from the people table
    cur.execute("SELECT id FROM people")
    people_ids = [row[0] for row in cur.fetchall()]

    relationship_types = ['friend', 'family', 'colleague', 'married']
    
    relationships = []
    for _ in range(100):
        person1_id, person2_id = random.sample(people_ids, 2)
        relationship_type = random.choice(relationship_types)
        start_date = fake.date_between(start_date='-10y', end_date='today')
        relationships.append((person1_id, person2_id, relationship_type, start_date))

    cur.executemany("INSERT INTO relationships (person1_id, person2_id, type, start_date) VALUES (?, ?, ?, ?)", relationships)
    con.commit()
    con.close()

if __name__ == '__main__':
    main()
