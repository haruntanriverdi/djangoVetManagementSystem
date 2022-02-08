# Django Vet Management System
Django Vet Management System Sample. 

## Usage
- Install virtualenv
```
cd path/to/project/folder
```

- Install virtualenv

```
$ pip install virtualenv
$ virtualenv venv
$ cd venv
$ source bin/activate
```

- Install requirements

```
$ pip install -r requirements.txt
```
- You can run the application with the following command:

```
$ python manage.py runserver
```
## Configuration
- You need to configure SECRET_KEY. To do this:

1- Create .env file in project folder

2- Write SECRET_KEY  save:

```
SECRET_KEY= secret_key
```
- You can create superuser using 
```
python manage.py createsuperuser
```
or, you can use pre created user informations which is
```
username: admin
password: djangoApp
```