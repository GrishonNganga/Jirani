# Awwards

#### An app that allows a user to be in the loop about everything happening in their neighbourhood.

####  Contributors:- **Grishon Ng'ang'a**,**Maryann Makena**,**Wilfred Muema**
         

## Setup/Installation Requirements

- To run the app, install `Python3`
- Then use these commands:
     1. `git clone https://github.com/GrishonNganga/Jirani.git`
     2. `cd Jirani`
     3. `python -m venv virtual` to create a virtual environment named `virtual`
     4. `source virtual/bin/activate` to activate the virtual environment
     5. `psql` then `CREATE DATABASE jirani` to create a postgres database
     6. `pip install -r requirements.txt` to install dependencies
     7. `python3 manage.py makemigrations neighbourhood` then `python3 manage.py migrate` to create database migrations
     8. `python3 manage.py runserver` to run the app
     9. `python3 manage.py test neighbourhood` to run the tests

## User stories
As a user I would like to:
  1. Sign in to the application to start using it.
  2. Set up a profile .
  3. Find a list of different businesses in my neighborhood.
  4. Find Contact Information for the emergency services (health department, fire department, and Police authorities) near my neighborhood.
  5. Create Posts that will be visible to everyone in my neighborhood.
  6. Change My neighborhood when I decide to move out.
  7. Users can only belong to one neighborhood at a time.
  8. Only view details of a single neighborhood.


## Known Bugs

No known bugs.

## Technologies Used

Django
Python3
Bootstrap4
HTML
CSS
Heroku

## Support and contact details

Incase of any issues drop me an email at maryann.makena00@gmail.com

### License

MIT License

Copyright (c) 2020 Makena-Maryann

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.