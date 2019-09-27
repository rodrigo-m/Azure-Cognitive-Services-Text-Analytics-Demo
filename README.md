# Azure Cognitive Services Text Analytics Demo
Python scripts to connect to Azure Text Analytics and extract Sentiment, Key Phrases, and Entities. Instructions are tested for VS Code running on Windows 10.

In this tutorial you will learn:
1. How to create a cognitive services endpoint for Text Analytics in Azure.
2. How to configure a script with credentials to access the text analytics endpoint.
3. How to call the text analytics service and display the results for sentiment score, entities, and key phrases. 
4. How to read text from a database and send it to text analytics in batches.
5. How to update a database with the results of text analytics calls. 

## Pre-requisites
1. VS Code installed.
    https://code.visualstudio.com/ 
    You can pick "user setup".
2. Access to an Azure subscription. 
    Get a free one here: https://azure.microsoft.com/en-us/free/search/ 
3. Connectivity to Azure cognitive services endpoints (https)
4. Python pre-requisites

4.1. Download and install Python for Windows
    https://www.python.org/downloads/
    Tutorial scripts tested with version 3.7.4

4.2. Install Python extension on VS Code
    https://marketplace.visualstudio.com/items?itemName=ms-python.python

4.3. Select a Python Interpreter
    Click on the lower left corner of VS Studio, select Python 3.7.x
For Additional details on Python installation and configuration, follow:
    https://code.visualstudio.com/docs/python/python-tutorial

4.4. Create and activate a Python environment in VS Code
    Ctrl+Shift+ to go to the Python terminal within VS Code, then run three commands:
        py -3 -m venv .venv
        Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
        .venv\scripts\activate

5. Install the Cognitive Services SDK
    Ctrl+Shift+ to go to the Python terminal
        python -m pip install azure-cognitiveservices-language-textanalytics --user
6. Install required Python libraries
     Ctrl+Shift+ to go to the Python terminal
        python -m pip install pyodbc
        python -m pip install pandas
        python -m pip install configparser
6. Install the ODBC driver for windows (for SQL connectivity)
    https://www.microsoft.com/en-us/download/details.aspx?id=56567
7. Download the scripts for the tutorial from GitHub:
        https://github.com/rodrigo-m/Azure-Cognitive-Services-Text-Analytics-Demo
        the click on "Clone or Download" then click "Download ZIP"
    if you have Git installed in your machine and have familiarity with Git you can clone the repository to a local drive:
      git clone https://github.com/rodrigo-m/Azure-Cognitive-Services-Text-Analytics-Demo.git
8. Open the folder where you saved the scripts from VS Code 
    File --> Open Folder...


# Tutorial steps

A total of 10 numbered scripts are needed for this tutorial. You will have five challenges during this tutorial where a partial script is provided and instructions to make the script work are after "TODO" tags within the script. 

Odd-numbererd scripts are incomplete and will not work. Even numbered scripts have working scripts with a solution to the challenge. We encourage you to try to fix the challenge script before looking at the solution. 

For example, the script "03. Entities One Call.py" does not work and the "TODO" tag within it outlines the challenge to make it work. The script "04. Entities One Call - Answer.py" is complete, with the answer to the challenge.

Credentials for all scripts are held in the config.ini file, and answer scripts will only work if the credentials are in place for each script. Configurations are structured as key-value pairs, as in the example below:
password = mypassword

There is no need for quotes, however an equal sign "=" is required between the key and the value.

Sections are used in the config.ini to group settings.

Start by creating a TExt Analytics cognitive service in the Azure Portal:
https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics

Continue from script "01. Sentiment One Call.py"




