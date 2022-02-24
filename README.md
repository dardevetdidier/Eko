# EKO - Budget management application
___
Work in Progress...

### Technologies

* Python 3.9.2
* Django 4.0.2
* Bootstrap 5

### Installation

* Clone this repository `https://github.com/dardevetdidier/Eko.git`
* Go to the root of the project\
`$ cd root/of/the/project`
* Create virtual environment\
`$ python -m venv venv`
* Activate virtual environment\
`$ source venv/Script/activate`
* Install packages\
`$ pip install -r requirements.txt`
* Migrations
`$ python manage.py migrate`
* Create a superuser
`$ python manage.py createsuperuser`

### How it works
- You can now run the server :
`$ python manage.py runserver`

- Access Application : http://127.0.0.1:8000

- You can login with your username and password created above.

- For the first use, go to 'Comptes' and create a new Account clicking 'Créer un Compte'.

- Before creating a new operation, it's recommanded to create categories which will be used to add operations.
(e.g. Rent, Food, Restaurant, Heating, ...). To create a category go to 'Categories' and click
on 'Créer une catégorie'. The new category will appear in the table and can be used when creating a new operation.