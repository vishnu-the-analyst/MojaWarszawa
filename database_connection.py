# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 20:06:40 2024

@author: Vishnu Kumar
"""

import mysql.connector
from datetime import datetime

endpoint = 'sql7.freesqldatabase.com'
username = 'sql7714154'
password = "UE9b4TPXsp"
database_name = 'sql7714154'


# Function to insert a new row into the messages table
def insert_message(data):
    # Connect to your MySQL database
    conn = mysql.connector.connect(host = endpoint,user = username, password = password, database = database_name)

    # Create a cursor object
    cursor = conn.cursor()

    # Extract information from the data
    user_id = str(data['message']['from']['id'])
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    message_id = f"{user_id}_{timestamp}"

    text = data['message'].get('text', data['message'].get('caption'))
    picture = None
    if 'photo' in data['message']:
        # Select the file_id of the highest resolution picture
        photo = max(data['message']['photo'], key=lambda x: x['file_size'])
        picture = photo['file_id']

    lon = data['message'].get('location', {}).get('longitude')
    lat = data['message'].get('location', {}).get('latitude')

    # SQL query to insert a new row
    insert_query = """
    INSERT INTO messages (message_id, user_id, timestamp, text, picture, lon, lat)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    # Data to be inserted
    record_to_insert = (message_id, user_id, timestamp, text, picture, lon, lat)

    # Execute the query
    cursor.execute(insert_query, record_to_insert)

    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

