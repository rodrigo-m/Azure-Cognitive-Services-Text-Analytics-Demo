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
                      "Server=" + config.get('database', 'server') + ";"
                      "Database=" + config.get('database', 'db_name') + ";"
                      "UID=" + config.get('database', 'user_name') + ";"
                      "PWD=" + config.get('database', 'user_password') + ";"
                      "Trusted_Connection=no;")

batch_size = 30
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

while (last_id <= max_id ):

    print ("processing last_id " + str(last_id))

    # Get the next batch of comments as a dataframe with id, language, text
    comments_df = pd.read_sql_query(
    next_batch_query.format(batch_size, last_id)
    , conn)

    # Converts the dataframe to a json string, then to a list of json docs (one item per row)
    documents = json.loads(comments_df.to_json(orient="records"))
    
    # Call the sentiment cognitive services
    response = text_analytics.sentiment(documents=documents)
    for document in response.documents:
        cursor = conn.cursor()
        cursor.execute("UPDATE dbo.reviews SET sentiment_score = ? WHERE id = ?", document.score, document.id)
        
    conn.commit()
    
    # get the maximum id processed in this batch
    last_id = int(comments_df['id'].max())


    






