# Assignment
Assignment db migration
This assignment was done using python django framework 
- to install the libraries required go to the root file of project where there is requirements.txt file present and give the command:
    pip install -r requirements.txt
    
- to run the project go to the project directory and give the commands:
      . python manage.py makemigrations (this command converts the models stored in the project to database tables)
      . python manage.py migrate (this creates the tables in the specified database along with the changes made)

to change the database to mysql :
   - go to settings.py file and go to the databases and change :
             'ENGINE': 'django.db.backends.postgresql_psycopg2',(for postgres)
             'ENGINE': 'django.db.backends.mysql'(for mysql and add ) 
             'ENGINE': 'mssql'('for sql server')
   - create a .env file inside the filepath mystask/mytask and give the database config in following manner:
         DB_NAME='Test'
         DB_USER='postgres'
         DB_PASSWORD='1234'
         DB_HOST='127.0.0.1'
         DB_PORT='5432'
