# mozio
Project 2.0

__Objective:__
Let transportation providers define their own custom polygons as service area to eliminate extra work load for Mozio employees.
1. Build a JSON REST API for transportation providers info, and thier service area.
2. Build an API endpoint to query service area data

__Main Libraries includes:__
- python-3.7.3
- django-2.2.1
- djangorestframework-3.10.1
- mysqlclient-1.3.14

__Virtual Environment:__
- Anaconda3 is used as virtual environment.
- Spec File venv_mozio_spec_file.txt can be used to install the environment with the following command:
    ```
    conda create --name env_name --file venv_mozio_spec_file.txt
    ```
- After creating he virtual environment, the following libraries has to be installed:
    ```
    pip install django-phone-field
    pip install django-language-field
    pip install django-mysql
    pip install Shapely
    ```
    
__Database:__

- Mysql is used as database.
- To setup database access:
    ```
    mysql -u root -p
    ```
- Create database transportation:
    ```
    CREATE DATABASE transportation;
    ```

__Django:__

- Ensure the database setting matches in mozio/mozio/settings.py (password should be updated):
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'transportation',
            'USER': 'root',
            'PASSWORD': '<password>',
            'HOST': '127.0.0.1',
            'PORT': '',
        }
    }
    ```

- Initial Django app with:
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```

- Unit tests can be ran to ensure Django app is installed correctly:
    ```
    python3 manage.py test
    ```
- To Run Django app:
    ```
    python3 manage.py runserver
    ```

__The API contains 3 main functions:__

1. To create, update, delete, and retreive information on Providers:
    Attributes include (all attrubutes must NOT be blank or Null):
    ```
    - Name
    - Email
    - Phone
    - Language
    - Curreny
    ```
    
    - To access data, visit:
        ```
        http://127.0.0.1:8000/providers/
        http://127.0.0.1:8000/providers/?format=json (for json format)
        ```
    
    - Provider content format:
        ```
        {
            "name": "",
            "email": "",
            "phone": "",
            "language": null,
            "currency": ""
        }
        ```
        Note: Language list can be found under HTML form.

2. To create, update, delete, and retreive information on Providers's service area: 
Attributes include (all attrubutes must NOT be blank):
    ```
    - Name
    - Provider <provider id>
    - Price (eg. 100.00)
    - Geojson File
    ```

    - To access data, visit:
        ```
        http://127.0.0.1:8000/service_area/
        http://127.0.0.1:8000/service_area/?format=json (for json format)
        ```

    - Service Area content format:
        ```
        {
          "provider": null,
          "name": "",
          "price": null,
          "geojson": null
        }
        ```
        Note: Provider list can be found under HTML form or enter provider id.
  
3. To query serice area with given lat/lng pair, and return a list of all polygons which include the give coords.
- Return attrubutes include: 
    ```
    -Provider Id
    -Prcvider Name
    -Polygon Name
    -Price
    ```
    - To query data, visit (specify lat/lng in url):
        ```
        http://127.0.0.1:8000/service_area_query/?lat=0.00&lng=0.00
        http://127.0.0.1:8000/service_area_query/?format=json&lat=0.00&lng=0.00 (for json format)
        ```

__Caching:__
- Django cache framework is used to cut as much overhead as possible:
- python-memcached is enabled in settings


    
