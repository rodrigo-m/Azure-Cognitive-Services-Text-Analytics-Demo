# To Connect with SQL Server
import pyodbc 
import pandas as pd
import json

# Cognitive Services Text Analytics SDK
from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from configparser import ConfigParser

# Load configuration from config.ini
config = ConfigParser()
config.read('config.ini')

# Retrieve connection settings from config.ini
access_key = config.get('text-analytics', 'access_key')
endpoint = config.get('text-analytics', 'endpoint')

# Connect to SQL Server
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=MININT-RB17R7E\SQL1;"
                      "Database=AirBnBSanFrancisco;"
                      "Trusted_Connection=yes;")

batch_size = 200
last_id = 0
max_id = 0

# Get the maximum id of the table to scan
max_id_query = "select max(id) as max_id from dbo.reviews"
comments_max_id_df = pd.read_sql_query(max_id_query, conn)
max_id = comments_max_id_df['max_id'].max()
print("max_id is " + str(max_id))

next_batch_query = "select top ({}) \
    CONVERT(nvarchar(12), id) AS [id], \
    'en' AS language, \
    comments AS [text] \
    from dbo.reviews \
    where id >  {} \
    and sentiment_score is null \
    order by id asc"

# Authenticate Text Analytics Client
credentials = CognitiveServicesCredentials(access_key)
text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)

# TODO: create a loop that (1) selects batches of records that do not have a sentiment_score
#       (2) calls text analytics to get the sentiment score
#       (3) updates the original record with the sentiment score.
#       Tip: you can run a cursor update for each response document with a command similar to:
#           cursor = conn.cursor()
#           cursor.execute("UPDATE dbo.reviews SET sentiment_score = ? WHERE id = ?", document.score, document.id)
#       Remember to close the update transaction with conn.commit()

while (last_id <= max_id ):

    print ("processing last_id " + str(last_id))

    # Get the next batch of comments as a dataframe with id, language, text
    # You can use comments_df = ...

    # Converts the dataframe to a json string, then to a list of json docs (one item per row)
  
    
    # Call the sentiment cognitive services

    # Update the records
    
    # get the maximum id processed in this batch
    # You can use last_id = int(comments_df['id'].max())


    






