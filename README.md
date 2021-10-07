# REST API - To Do App

This is a rest api build using `django_rest_framework` to serve a to do app.

## Build with

- [django_rest_framework](https://www.django-rest-framework.org)

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

## Usage

- Register endpoint

```sh
POST api/register
```

```sh
{
   "email": "email",
   "username": "your_username",
   "password": "your_password"
}
```

- Login endpoint

```sh
POST api/login
```

```sh
{
   "username": "your_username",
   "password": "your_password"
}
```

For the endpoints bellow, a auth token is required.

- Get todos endpoint for user

```sh
GET api/todo-list
```

- Create a new to do

```sh
POST api/todo-create
```

```sh
{
   "text": "your_text"
}
```

- Delete to do

```sh
DELETE api/todo-delete/<str:pk>
```

- Update to do

```sh
PUT api/todo-update/<str:pk>
```
