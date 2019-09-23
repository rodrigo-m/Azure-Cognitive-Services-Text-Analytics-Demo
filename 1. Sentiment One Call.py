from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from configparser import ConfigParser

# TODO: open the file config.ini and replace the strings under the "text-analytics" section
# Steps:
# 1. Use the Azure portal to create a Text Analytics Cognitive Service
# 2. Get the Endpoint URL and the Access Key 1 from the Azure Portal and adjust the config.ini file 

# Read configuration from config.ini
config = ConfigParser()
config.read('config.ini')

# Retrieve connection settings from config.ini
# TODO: replace the name of the keys in the next line with what you found in config.ini
access_key = config.get('text-analytics', '<key name for the access key>')
endpoint = config.get('text-analytics', 'endpoint')

print("Access key: " + access_key)
print("Endpoint: " + endpoint)

# Using access key as credential
credentials = CognitiveServicesCredentials(access_key)

# Authenticate Client
text_analytics = TextAnalyticsClient(endpoint=endpoint, credentials=credentials)

# Build input documents
documents = [
    {
        "id": "1",
        "language": "en",
        "text": "I had the best day of my life."
    },
    {
        "id": "2",
        "language": "en",
        "text": "I had the worst day in my existence."
    }  
]

# Call the Cognitive Service
response = text_analytics.sentiment(documents=documents)

#Display the results
for document in response.documents:
    print("Document Id: ", document.id, ", Sentiment Score: ",
          "{:.2f}".format(document.score))