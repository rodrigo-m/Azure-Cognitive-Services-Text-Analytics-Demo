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

# Build a connection object to  Connect to SQL Server 
# TODO: adjust the config.ini with the connection settings for your database
conn = pyodbc.connect("Driver={SQL Server};"
                      "Server=" + config.get('database', 'server') + ";"
                      "Database=" + config.get('database', 'db_name') + ";"
                      "UID=" + config.get('database', 'user_name') + ";"
                      "PWD=" + config.get('database', 'user_password') + ";"
                      "Trusted_Connection=no;")

# Build the query to retrieve documents from the database
# TODO: try the script with the query below, which will get 20 recprds. If it works, modify  
#       the query so that (1) it selects only records that have a NULL sentiment_score 
#       and (2) the number of records sent to the text analytics service is controlled 
#       by a variable. 
query = "select top (20) \
    CONVERT(nvarchar(12), id) AS [id], \
    'en' AS language, \
    comments AS [text] \
    from dbo.reviews \
    order by id asc"

# Connect, query, and create a dataframe with the results ( id, language, text )
comments_df = pd.read_sql_query(query, conn)

# Authenticate Text Analytics Client
credentials = CognitiveServicesCredentials(access_key)
text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)

# Converts the dataframe to a json string, then to a list of json docs (one item per row)
documents = json.loads(comments_df.to_json(orient="records"))
# List of JSON docs looks like this: [ {...} , {...} ]

# Call the sentiment cognitive services
response = text_analytics.sentiment(documents=documents)

# Display the results
for document in response.documents:
    print("Document Id: ", document.id, ", Sentiment Score: ",
        "{:.2f}".format(document.score))