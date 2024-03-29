from dotenv import load_dotenv
import os
import psycopg2
import requests
import time

load_dotenv()
API_KEY = os.environ.get("API_KEY")

# Setup connection to Database
conn = psycopg2.connect(database="riotdb", user="jake", password="password", host="localhost", port="5432")
cursor = conn.cursor()

# Jan 11th 2024 @ 2:00 UTC, babe wake up, new map dropped.
newMapEpoch = 1704938400

# Query only puuid column
query = "SELECT puuid, region, tier FROM summoners;"
cursor.execute(query)

# Get all rows
results = cursor.fetchall()

# Close the cursor for SELECT Query
cursor.close()

#regions = ['BR1', 'EUN1', 'EUW1', 'JP1', 'KR', 'LA1', 'LA2', 'NA1',
#          'OC1', 'PH2', 'RU', 'SG2', 'TH2', 'TR1', 'TW2', 'VN2']

def map_region(value):
    region_mapping = {
        'BR1': 'AMERICAS',
        'NA1': 'AMERICAS',
        'LA1': 'AMERICAS',
        'LA2': 'AMERICAS',
        'EUN1': 'EUROPE',
        'EUW1': 'EUROPE',
        'TR1': 'EUROPE',
        'RU': 'EUROPE',
        'KR': 'ASIA',
        'JP1': 'ASIA',
        'OC1': 'SEA',
        'PH2': 'SEA',
        'SG2': 'SEA',
        'TH2': 'SEA',
        'TW2': 'SEA',
        'VN2': 'SEA'
    }

    return region_mapping.get(value, 'UNKNOWN')

cursor = conn.cursor()

for row in results:
    region = map_region(row[1])
    tier = row[2]
    r = requests.get(f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{row[0]}/ids?startTime={newMapEpoch}&type=ranked&start=0&count=100&api_key={API_KEY}').json()
    for match in r:
        query = f"INSERT INTO matches (matchid, region, tier, queried) VALUES (%s, %s, %s, %s)"
        values = (str(match), region, tier, False)
        try:
            # Execute INSERT Statement
            cursor.execute(query, values)

            # Commit changes to Database
            conn.commit()
                
            print("Data inserted successfully.")
        except (Exception, psycopg2.Error) as error:
            # Roll back the transaction in case of an error:
            conn.rollback()
            print("Error inserting data:", error) 

# Close cursor and db connection
cursor.close()
conn.close()
