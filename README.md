# Throttle

A simple python based server to display user activity data.

## Steps

1. Clone this repository to your local.

2. Open the project in an editor of your preference.

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

    ```bash
      pip install django
    ```
4. Run your server

   ```bash
      python manage.py runserver 
    ```
   or, the below command if your default python version is python2 use [python3](https://www.python.org/downloads/)

    ```bash
      python3 manage.py runserver 
    ```

5. Your server should be up and running now.

## Endpoints

There are two endpoints to get the desired result.

1. `/getUserActDetails` : To get all user's activity data. It's a **get** api.

2. `/getAllUsers` : To get all users. It's a **get** api.


## Tables

+ **User**

  This table contains the details of the user. There are 4 columns in this table

   - **id** : Contains the index of the user data row.
   - **user_id** : Contains the unique userId of the user. This is also used as ***Foreign Key*** in the ***ActivityModel*** table.
   - **real_name** : It contains the name of the user.
   - **tz** : Contains the timezone detail of the user.

+ **ActivityPeriod** 

  This table contains the activity data of the users. There are 4 columns in this table

   - **id** : Contains the index of the user activity data row.
   - **user_id** : Foreign key to map activity data to the user it belongs to from the ***User*** table.
   - **start_time** : Start time of the activity.
   - **end_time** : End time of the activity.



   The Server is also hosted at [PythonAnywhere](https://www.pythonanywhere.com/). Click on the below links to use it directly from the hosted server.

   + [GetAllUser](http://abhinavanand499.pythonanywhere.com/getAllUsers/)
   + [Get Activity Data of all users](http://abhinavanand499.pythonanywhere.com/getUserActDetails/)



   ***Note : All Data being used is dummy data. Also database mapping is not done as it was not needed in Assesment***
               


   **Thank You :)**
