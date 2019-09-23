from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from configparser import ConfigParser

# Load configuration from config.ini
config = ConfigParser()
config.read('config.ini')

# Retrieve connection settings from config.ini
access_key = config.get('text-analytics', 'access_key')
endpoint = config.get('text-analytics', 'endpoint')

# Use access key as credential
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