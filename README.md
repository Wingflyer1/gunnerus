# Reserver
Python, Django and SQLite-based cruise reservation system

## Mockup
http://gunnerus.471.no

## ER diagram
https://drive.google.com/file/d/0B12qJja_kwUTSG9naHl1X3hiSmc/view?usp=sharing

## Structure
 - The "reserver" app is intended to encapsulate the main functionality of the reservation system. Other stuff will be placed in separate apps as appropriate during the development process.

## Installation notes
 - Requires (virtual) environment with Django, django-extra-views and django-bootstrap3
 - Typical dev setup:
      - Working directory with two folders, "env" and "gunnerus"
      - "gunnerus" folder contains this repository
      - "env" contains a virtual Python 3 environment
      - Set up using...
           - virtualenv env
           - env\Scripts\activate
           - pip install -r requirements.txt
      - Run using "python manage.py runserver" as usual
      - Use "deactivate" to stop using the virtual environment when you're done
      - If you run into issues with database tables not being created on the initial run of the server, use migrate --run-syncdb.
