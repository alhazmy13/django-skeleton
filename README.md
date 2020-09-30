# Django Skeleton

---
**NOTE**

This repo is not done yet, i'm still working here :D

---

![License](https://img.shields.io/badge/license-MIT-green.svg)
[![Coverage Status](https://coveralls.io/repos/github/alhazmy13/django-skeleton/badge.svg?branch=master)](https://coveralls.io/github/alhazmy13/django-skeleton?branch=master)
[![Build Status](https://travis-ci.com/alhazmy13/django-skeleton.svg?branch=master)](https://travis-ci.com/alhazmy13/django-skeleton)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?longCache=true)
![Python Versions](https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7%20%7C%203.8-blue.svg)


# Overview

*Django Skeleton* is built on top of the Django rest framework with some modifications.

## Contents

* [Requirements](#requirements)
* [Installing](#installing)
* [Deploy](#deploy-to-aws)
* [Run it locally](#run-it-locally)
* [Swagger and Documentation](#swagger-and-documentation)
* [Configuration](#configuration)
* [Authentication ](#authentication)
    + [Obtain Token](#obtain-token)
    + [Refresh Token](#refresh-token)
* [Structure](#structure)
  + [Custom User Model](#custom-user-model)
  + [Create a new app](#create-a-new-app)
* [Testing](#testing)


## Requirements

* `python` (Python 3.x)
* `pip` (python package manager)

## Installing
WIP

## Deploy

WIP

## Configuration
WIP

## Authentication 
For this skeleton we are used [djangorestframework_simplejwt](https://github.com/SimpleJWT/django-rest-framework-simplejwt) library, all tokens will be as JWT tokens, The JWT is acquired by exchanging an email + password for an access token and an refresh token.
The access token is usually short-lived (expires in 5 min or so, can be customized though).
The refresh token lives a little bit longer (expires in 24 hours, also customizable). It is comparable to an authentication session. After it expires, you need a full login with email + password again.


#### Obtain Token

First step is to authenticate and obtain the token. The endpoint is /api/token/ and it only accepts POST requests.

```python 
http post http://127.0.0.1:8000/api/token/ email=vitor password=123
```
So basically your response body is the two tokens:
```python
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjU5LCJqdGkiOiIyYmQ1NjI3MmIzYjI0YjNmOGI1MjJlNThjMzdjMTdlMSIsInVzZXJfaWQiOjF9.D92tTuVi_YcNkJtiLGHtcn6tBcxLCBxz9FKD3qzhUg8",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTMxMDM1OSwianRpIjoiMjk2ZDc1ZDA3Nzc2NDE0ZjkxYjhiOTY4MzI4NGRmOTUiLCJ1c2VyX2lkIjoxfQ.rA-mnGRg71NEW_ga0sJoaMODS5ABjE5HnxJDb0F8xAo"
}
```
In order to access the protected views on the backend (i.e., the API endpoints that require authentication), you should include the access token in the header of all requests, like this:

```python
http http://127.0.0.1:8000/hello/ "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQ1MjI0MjAwLCJqdGkiOiJlMGQxZDY2MjE5ODc0ZTY3OWY0NjM0ZWU2NTQ2YTIwMCIsInVzZXJfaWQiOjF9.9eHat3CvRQYnb5EdcgYFzUyMobXzxlAVh_IAgqyvzCE"
```

#### Refresh Token
To get a new access token, you should use the refresh token endpoint /api/token/refresh/ posting the refresh token:

```python
http post http://127.0.0.1:8000/api/token/refresh/ refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU0NTMwODIyMiwianRpIjoiNzAyOGFlNjc0ZTdjNDZlMDlmMzUwYjg3MjU1NGUxODQiLCJ1c2VyX2lkIjoxfQ.Md8AO3dDrQBvWYWeZsd_A1J39z6b6HEwWIUZ7ilOiPE
```

The return is a new access token that you should use in the subsequent requests.

## Swagger and Documentation
This skeleton will generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API using [drf-yasg](https://github.com/axnsan12/drf-yasg); this exposes four endpoints:

* A JSON view of your API specification at `/swagger.json`
* A YAML view of your API specification at `/swagger.yaml`
* A swagger-ui view of your API specification at `/swagger/`
* A ReDoc view of your API specification at `/redoc/`

## Structure

This is the directory structure; I will explain it and update it later :D

```
mysite
├── mysite
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── apps
│   ├── __init__.py
│   └── users
│       ├── __init__.py
│       ├── admin.py
│       ├── models.py
│       ├── tests.py
│       └── views.py
└── manage.py
```

### Custom User Model 
In this skeleton, we used a custom User model so that an email address can be used as the primary user identifier instead of a username for authentication. If you want to change it back to username, then update `apps>users>model.py`

```python
class CustomUser(AbstractBaseUser, PermissionsMixin):
    ...
    username = models.EmailField(_('username'), unique=True)
    ...
    USERNAME_FIELD = 'username'
```


### Create a new app
We moved the apps to sub-directory, and because of that, if you want to create a new app, use the default command line, and then move the folder to `apps` directory:
```python
python manage.py mysecondapp
mv mysecondapp apps/
```

**Warning: Don't be tempted to call `python manage.py ./apps/mysecondapp`. This deletes all other apps in that directory.**

## Testing
WIP