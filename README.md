# OC_P12_Poullain_Arthur
CRM Using Django Rest API

# How to install ?
* Clone the Repository : ```$ git clone https://github.com/Barbecuecitron/OC_P12_Poullain_Arthur ```

# Prepare a virtual env
* Create a new environment ``` $python -m venv MyEnv ```
* Activate the env with ``` $MyEnv\Scripts\Activate ```
* Install the required libraries in the env ``` $pip install -r \path\to\repository\requirements.txt ```


# Setup a PostgreSQL DB in order to run the project
* Install [PostGreSQL](https://www.postgresql.org/)
* Create a PostgreSQL DB using PGAdmin or PSQL
* Link your DB to the app using the project/settings.py file
* Run ``` python manage.py migrate ``` to populate you newly created DB from the included migrations files.

# How to use ?
* Run ``` python manage.py runserver ``` to launch the local server.
