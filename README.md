# Rumour-Tweet-Detection
Twitter

Rumour Tweet Detection is a web application which detects whether the mentioned tweet is a rumored tweet or not using Machine Learning Algorithm. Link of the deployed web application : https://rumor-tweet-detector.herokuapp.com/


## Directory Structure
- Requirements.txt: contains all the dependencies required for the web application.
- Procfile.txt: requires to set up heroku
- App.py: contains the main function required to run the flask application
- model: contains the trained model and tfidf variable 
- templates: contain the mail html file which will render when running the application

## Introduction
Rumour Tweet Detection application has been built purely on python programming language. This application has been deployed using Flask web framework and then hosted on Heroku servers.
 
## Project Execution
- Open the terminal
- Clone this repository using: https://github.com/akanshagautam3751/Rumor-Tweets-Detector.git 
- Create a virtual environment for the application to work
- Activate the virtual environment
- Make sure your system has pip and python installed
- Download all the dependencies in requirements.txt using pip install -r requirements.txt
- Don't forget to import nltk. Execute nltk.download('stopwords')
- To run the application, hit python app.py. It will take you to http://127.0.0.1:5000/

