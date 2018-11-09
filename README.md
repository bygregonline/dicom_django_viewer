---
---

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.11-brightgreen.svg)](https://djangoproject.com)
[![Django Version](https://img.shields.io/badge/matlotlib-3.00-brightgreen.svg)](https://matplotlib.org/)

**Author:** Gregorio Flores

**web:** www.aniachitech.com

**email:** gregorio.flores


# DICOM FILE VIEWER 
---

[![](http://img.youtube.com/vi/PkrC3QAfWSE/0.jpg)](http://www.youtube.com/watch?v=PkrC3QAfWSE "Youtube")

---

What is a DICOM file

A DICOM file is an image saved in the Digital Imaging and Communications in Medicine (DICOM) format. It contains an image from a medical scan, such as an ultrasound or MRI. DICOM files may also include identification data for patients so that the image is linked to a specific individual.



# Step by step Django tutorial

## Running the Project

First, install python on your local computer:

```bash
brew install python3 tree 
```

Install the requirements:

```bash
pip install matplotlib numpy django termcolor imageio
```


Create a directory :

```bash
mkdir myproject
cd myproject
```

Create a  new django project :

```bash
django-admin startproject myproject
```

Create a  new django project :

```bash
django-admin startproject myproject
```

See and verify your directory structure

```bash

├── manage.py
└── myproject
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Create a  new django application   :

```bash
 django-admin startapp dicom
```



See and verify your directory structure

```bash
.
├── dicom
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── myproject
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

add dicom to setting.py
 
```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dicom',
]
```


TODO FINISH

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.


