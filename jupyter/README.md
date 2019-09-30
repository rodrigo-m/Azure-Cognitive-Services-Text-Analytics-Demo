# Azure Cognitive Services Text Analytics Demo
Python scripts in Jupyter notebooks to connect to Azure Text Analytics and extract Sentiment, Key Phrases, and Entities. Instructions are tested in a Azure Machine Learning Notebook VM with Azure ML and Kernel - Python 3.6 AzureML.

In this tutorial you will learn:
1. How to create a cognitive services endpoint for Text Analytics in Azure.
2. How to configure a script with credentials to access the text analytics endpoint.
3. How to call the text analytics service and display the results for sentiment score, entities, and key phrases. 
4. How to read text from a database and send it to text analytics in batches.
5. How to update a database with the results of text analytics calls. 

## Pre-requisites
1. Create an Azure Machine Learning Workspace and a 
    Follow the instrucions on the page below only, stop at "Next Steps"
    https://docs.microsoft.com/en-us/azure/machine-learning/service/tutorial-1st-experiment-sdk-setup   
2. Clone the repository with ipynb notebooks
    Launch Jupyter notebooks from the Azure Machine Learning Workspace
    Fromt he top left of your screen, click New --> Terminal 
    From the terminal prompt go to the directory you would like to copy the files to
    Type the command below:
      git clone https://github.com/rodrigo-m/Azure-Cognitive-Services-Text-Analytics-Demo.git
    Close the browser tab with the terminal window
3. Install required Python libraries
    Open the folder Azure-Cognitive-Services-Text-Analytics-Demo
    Open the folder "jupyter"
    Open the notebook "00. Install Libraries.ipynb"
    Run each cell of the notebook above to install the required libraries
    Close the tab with the "00. Install Libraries.ipynb" notebook

# Tutorial steps

A total of 10 numbered notebooks are needed for this tutorial. You will have five challenges during this tutorial where a partial script is provided and instructions to make the script work are after "TODO" tags within the script. 

Odd-numbererd notebooks are incomplete and will not work. Even numbered notebooks have working scripts with a solution to the challenge. We encourage you to try to fix the challenge script before looking at the solution. 

For example, the script "03. Entities One Call.py" does not work and the "TODO" tag within it outlines the challenge to make it work. The script "04. Entities One Call - Answer.py" is complete, with the answer to the challenge.

Credentials for all scripts are held in the config.ini file, and answer scripts will only work if the credentials are in place for each script. Configurations are structured as key-value pairs, as in the example below:
password = mypassword

There is no need for quotes in the config.ini file, however an equal sign "=" is required between the key and the value.

Sections are used in the config.ini to group settings.

Start this tutoria from script "01. Sentiment One Call.py"




