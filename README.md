# REST API - To Do App

This is a rest api build using `django_rest_framework` to serve a to do app.

## Prerequisites

- `python 3`
- `pip`
- `virtualenv`

## Installation

1. Clone repo
2. Create virtual env
   ```sh
   virtualenv env_name
   ```
3. Activate env
   ```sh
   . env_name/bin/activate
   ```
4. Install required modules
   ```sh
   python3 -m pip install -r requirments.txt
   ```
5. Make migrations for db
   ```sh
   python3 manage.py make migrations
   python3 manage.py migrate
   ```
