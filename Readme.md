### Get the codebase

1. Clone the repo: `git clone https://github.com/hypebalaga/hb-port1.git`

### Creating and running the virtual environment. Needs python3

Create:

    virtualenv venv -p python3 or
    python3 -m virtualenv venv
    (For windows: `py -3 -m venv .`)

Run:

    source venv/bin/activate

    (For windows: `Scripts\activate`)

### Installing dependencies and running the server

`pip install -r requirements.txt`

`source environ.txt`

`python manage.py migrate`

`python manage.py createsuperuser`

**Provide superuser credentials**

`python manage.py runserver`
