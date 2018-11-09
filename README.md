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

**Categories**

1.	medical scientists 
3.	data scientific
4.	nerds
5.	technology enthusiasts
6.	python developers
7.	django developers

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

Add dicom to setting.py
 
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

Create 3 directories inside myproject
 
```bash
mkdir temp
mkdir static_content
mkdir templates

tree

    ├── static_content
    ├── temp
    ├── templates

```

Modiffy setting.py

```bash
#Add this lines
STATICFILES_DIRS = [(
    os.path.join(BASE_DIR, 'myproject/static_content')
),]


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'myproject/temp')
]

#And modiffy templates 
#Add 'DIRS': [os.path.join(BASE_DIR, 'myproject/templates')]',
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'myproject/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



```


Put the static content

Create the template 
---
---

Run the development server:

```bash
python manage.py runserver
```

Verify the server status

```bash
curl -I  http://127.0.0.1:8000/static/img/logo.png 
response 
HTTP/1.1 200 OK
Date: Tue, 06 Nov 2018 23:20:11 GMT
Server: WSGIServer/0.2 CPython/3.7.0
Content-Type: image/png
Content-Length: 14235
Last-Modified: Mon, 21 May 2018 23:48:49 GMT
```

edit setting.py

```bash
remove 
    'django.middleware.csrf.CsrfViewMiddleware',
```

Crete views.py inside  dicom directory

```bash
touch views.py
```
Add this two functions  

```bash
import base64
import os
import time
import traceback
from io import BytesIO

import imageio
import matplotlib.pyplot as plt
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import redirect, render
from termcolor import colored

from myproject import settings

#our page
def app_render(request):
    print(settings.BASE_DIR)
    d = {'title': 'DICOM viewer','info':'DICOM SERVER SIDE RENDER'}
    return render(request, "main_template.html", d)
 

#just to redirect to the web app   
def send_to_dcom(request):
   return redirect('medical/app')

```

Modiffy urls.py 

```bash
from dicom import views
from django.urls import path


urlpatterns = [
    path('', views.send_to_dcom),
    path('medical/app',views.app_render),
    
```

Test your app

![png](https://raw.githubusercontent.com/bygregonline/dicom_django_viewer/master/images/image1.png)

add your webservice into views.py

```bash

def ajax_server(request):
    start = time.time()
    d = dict()
    generic = dict()
    medinfo = dict()

    try:

        print('FILE--->',str(request.FILES['imgInp'])[-3:])

        if request.method == 'POST' and ('imgInp' in request.FILES) and request.FILES['imgInp'] and  str(request.FILES['imgInp'])[-3:].upper() =='DCM':
            file = request.FILES['imgInp']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            full_path_file = os.path.join(settings.MEDIA_ROOT, filename)
            print(colored('path->', 'red'), full_path_file)

            generic['name'] = filename
            generic['size'] = os.path.getsize(full_path_file)
            try:
                if full_path_file[-3:].upper() == 'DCM':
                    dcpimg = imageio.imread(full_path_file)
                    for keys in dcpimg.meta:

                        medinfo[keys] = str(dcpimg.meta[keys])

                    if len(dcpimg.shape) ==4:
                        dcpimg = dcpimg[0,0]
                    elif len(dcpimg.shape) ==3:
                        dcpimg = dcpimg[0]

                    fig = plt.gcf()
                    fig.set_size_inches(18.5, 10.5)
                    plt.imshow(dcpimg, cmap='gray')
                    plt.colorbar()
                    figure = BytesIO()
                    plt.savefig(figure, format='jpg', dpi=300)

                    plt.close()
                    d['url'] = {'base64': 'data:image/png;base64,' + base64.b64encode(figure.getvalue()).decode()}

                # medinfo.update(dcpimg.meta)

            except Exception as e:

                traceback.print_tb(e)





            fs.delete(filename)
    except Exception as e:
        traceback.print_tb(e)




    generic['process time'] = time.time() - start
    d['generic'] = generic


    d['med'] = medinfo


    print(colored(d, 'red'))
    return JsonResponse(d)

    
```


add the url into. urls.py
      
```bash
path('medical/process.ajax',views.ajax_server),
```


The project will be available at **127.0.0.1:8000**.

#Enjoy it

