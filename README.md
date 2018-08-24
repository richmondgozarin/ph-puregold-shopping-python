# ph-puregold-shopping-python

# Technologies used:
- Flask
- Flask Restful
- Flask Api
- SQL Alchemy


# Installation:

Clone the project repo
`$ git clone https://github.com/ph-puregold-shopping-python.git`
`$ cd ph-puregold-shopping-python`

Create Virtual env:
`$ python3 -m venv venv`

Acticate venv:
`$ . venv/bin/activate`

Install dependencies
`$ pip3 install -r requirements.txt`

# Run local
`$ ./run_local.sh`

# Endpoints:
List - `http://127.0.0.1:5000/shoppings`
View - `http://127.0.0.1:5000/shoppings/<shopping_id>`
Post - `http://127.0.0.1:5000/shoppings`
Put  - `http://127.0.0.1:5000/shoppings/<shopping_id>`
Delete - `http://127.0.0.1:5000/shoppings/<shopping_id>` 

TODO:
Integrate SQL-Alchemy

Resources:
https://flask-restful.readthedocs.io/en/latest/quickstart.html
