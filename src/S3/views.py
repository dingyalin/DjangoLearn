# encoding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from .models import Path

import os

# Create your views here.
def list_file(request, perfix=""):
    context = {}
    current_path = Path.objects.filter(name=perfix)[0]
    current_path_id = current_path.id
    path_list = Path.objects.filter(up_path_id=current_path_id)
    file_list = current_path.file_set.all()
 
    context['path_list'] = path_list
    context['file_list'] = file_list
    
    return render(request, 'S3/S3.html', context)

def upload(request):  
    #assert False
    if request.method == "POST":    # 请求方法为POST时，进行处理  
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None  
        if not myFile:  
            return HttpResponse("no files for upload!")  
        destination = open(os.path.join("D:\\upload",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作  
        for chunk in myFile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()  
        return HttpResponse("upload over!")  
    
def download(request):
    # do something...
    filename = "D:\\upload\\EcsAgentRestart.zip"
        
    def file_iterator(filename, chunk_size=512):
        with open(filename, "rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
                

    response = StreamingHttpResponse(file_iterator(filename))
    
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename=%s' % "EcsAgentRestart.zip"
    
    print response

    return response

