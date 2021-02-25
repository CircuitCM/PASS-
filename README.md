# PASS-
Machine Learning-based Performance Evaluation Web Platform for D3, Club and High School Sports Programs 


```This documentation is for a Windows system; adjust accordingly```

Pass Analytics Machine Learning Code (Prediction Model):
1.	Clone GitHub repo and open ```xG Model``` folder in development environment that supports Python (e.g. VSCode, PyCharm, IntelliJ, etc.)

2.	Python Module Installation (via Command Prompt):
  - Numpy (scientific computing): ```pip install numpy```
  - Pandas (data manipulation): ```pip install pandas```
  - Scikit-Learn (ML model construction): ```pip install -U scikit-learn```
  - Seaborn (data visualization): ```pip install seaborn```
  - Matplotlib (data visualization): ```pip install matplotlib```
  - Pygsheets (Google Sheets connectivity): ```pip install pygsheets```
      - My Google credentials will not be included in the repo, so follow this step-by-step guide for authorizing your own pygsheets: 
      https://pygsheets.readthedocs.io/en/latest/authorization.html

3.	Code Execution:
  - Read in desired test and training data sets via Google Spreadsheet or local .csv file.
    - Download project training set ```events.csv``` from https://www.kaggle.com/gabrielmanfredi/expected-goals-player-analysis?select=events.csv
  - If updating existing Google Spreadsheet with prediction results: establish connection to specific spreadsheet via pygsheets. 
  - If operating locally: include additional code to export output as .csv file for future use, or simply execute program without use of pygsheets. 
  - Run ```dataMain.py``` to execute MoBot xG prediction model. 
  - To create data visualizations: input spreadsheet data into ```dataViz.py``` , adjust to specifications, and execute. 

Pass Analytics Web Development Code (Flask Web App):
1.	Clone GitHub repo and open ```Flask App``` folder in development environment

2.	Module/Library Installation:
  -	Flask (Python web framework): ```pip install Flask```
  -	Pandas (if not already installed): ```pip install pandas```
  -	Pygsheets (if not already installed): ```pip install pygsheets```
    - My Google credentials will not be included in the repo, so follow this step-by-step guide for authorizing your own pygsheets: https://pygsheets.readthedocs.io/en/latest/authorization.html
  -	Gunicorn (Python WSGI HTTP Server): ```pip install gunicorn```

3.	Running Web App Locally:
  -	Alter HTML/CSS/JavaScript as desired (or leave it alone)
  -	Type ```app.py``` on the command line and click Enter.
  - Example:
    ```
    C:\Users\..\..\FlaskApp>app.py
     * Serving Flask app "app" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Restarting with windowsapi reloader
     * Debugger is active!
     * Debugger PIN: xxx-xxx-xxx
     * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    ```
4.	Deploying Web App via Heroku (refer to links below):
  -	https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/
  -	https://stackabuse.com/deploying-a-flask-application-to-heroku/

  - Note: other hosting options can be used, but this specific project makes use of Heroku. 

      - Heroku Alternatives: https://blog.back4app.com/heroku-alternatives/
