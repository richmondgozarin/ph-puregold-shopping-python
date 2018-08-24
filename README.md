# ph-puregold-shopping-python

# Technologies used:
- Flask
- Flask Restful
- Flask Api
- SQL Alchemy


# Installation:

Open Terminal and clone the project repo:

`$ git clone https://github.com/ph-puregold-shopping-python.git`

`$ cd ph-puregold-shopping-python`

Create Virtual env:

`$ python3 -m venv venv`

Acticate venv:

`$ . venv/bin/activate`

Install dependencies:

`$ pip3 install -r requirements.txt`

Create Database in this case `sqlite`:

`$ cd $HOME`

`$ mkdir sqlite`

`$ cd sqlite`

`$ sqlite3 ShoppingDB.db`

Once database is created, create table schema:

copy schema from `schema.sql` and paste it to sqlite3 instance.

# Run local

`$ ./run_local.sh`

# Shopping list Endpoints:

List - `http://127.0.0.1:5000/shopping`

View - `http://127.0.0.1:5000/shopping/<shopping_id>`

Post - `http://127.0.0.1:5000/shopping`

Put  - `http://127.0.0.1:5000/shopping/<shopping_id>`

Delete - `http://127.0.0.1:5000/shopping/<shopping_id>` 

# Shopping Item Endpoints:

List - `http://127.0.0.1:5000/item`

View - `http://127.0.0.1:5000/item/<item_id>`

Post - `http://127.0.0.1:5000/item`

Put  - `http://127.0.0.1:5000/item/<item_id>`

Delete - `http://127.0.0.1:5000/item/<item_id>` 


Resources:
https://flask-restful.readthedocs.io/en/latest/quickstart.html
