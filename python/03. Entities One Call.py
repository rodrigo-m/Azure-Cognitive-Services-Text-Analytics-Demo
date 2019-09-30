from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
from configparser import ConfigParser
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

# Sample document with text
documents = [
    {
        "id": "1",
        "language": "en",
        "text": "Microsoft was founded by Bill Gates and Paul Allen on April 4, 1975, to develop and sell BASIC interpreters for the Altair 8800."
    }
]

# Extract entities. 
# TODO: Add code here that calls Text Analytics and extracts entities


# Display the results
for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Entities:")
    for entity in document.entities:
        print("\t\t", "NAME: ", entity.name, "\tType: ",
              entity.type, "\tSub-type: ", entity.sub_type)
        for match in entity.matches:
            print("\t\t\tOffset: ", match.offset, "\tLength: ", match.length, "\tScore: ",
                  "{:.2f}".format(match.entity_type_score))