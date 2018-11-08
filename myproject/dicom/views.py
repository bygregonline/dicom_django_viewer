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


def send_to_dcom(request):
   return redirect('medical/app')


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





def app_render(request):
    print(settings.BASE_DIR)
    d = {'title': 'DICOM viewer','info':'DICOM SERVER SIDE RENDER'}
    return render(request, "main_template.html", d)




