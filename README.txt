Django website for TGV information browsing.
Fontionality:
    - "Search" - select a specific departure and destionation station: show its price
    - "Inspire me" - select a specific departure station: show all possible destinations and theirs price

Future work:
    - Update placemarks and paths for "Search" and "Inspire me" 
    - Make the interface prettier

Requirements:
    - Python 2.7
    - Django 1.11
    - MongoDB 3.4
    - Pymongo
    - Mongoengine

Please generate the following command for setting environment:

    sudo apt-get install python python-virtualenv
    virtualenv .env
    source .env/bin/activate
    sudo pip install -U setuptools
    pip install --requirement requirements.txt

Please make sure that your machine is installed MongoDB, if not check here:
    https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
 
Dumping/loading database:
    python gares_save.py
    python tarif_save.py

Upgrading migrations:
    rm -rf tgv/migrations/
    python manage.py makemigrations
    python manage.py migrate

Run server:
    python manage.py runserver

Url examples:
    http://localhost:8000/browse/
    http://localhost:8000/find/?depart=87746008&destination=87481002
    http://localhost:8000/inspire/?depart_inspire=87747006
