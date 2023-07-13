from django.shortcuts import render
from rest_framework.decorators import api_view
import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .models import *
from .serializers import *
from django.views import View
from django.core.files.storage import FileSystemStorage

# Create your views here.

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# class  object(View):
#     def obj(self, request):
#         form = DetectSerializers(request.POST, request.FILES)
#         if form.is_valid():
#             # this `initial_obj` if you need to update before it uploaded.
#             # such as `initial_obj.user = request.user` if you has fk to `User`, 
#             # if not you can only using `obj = form.save()`
#             initial_obj = form.save(commit=False)
#             initial_obj.save()

#             # return path name from `upload_to='documents/'` in your `models.py` + absolute path of file.
#             # eg; `documents/filename.csv`
#             print(initial_obj.document)

#             # return `MEDIA_URL` + `upload_to` + absolute path of file.
#             # eg; `/media/documents/filename.csv`
#             print(initial_obj.document.url)
              

        # create video capture object
@api_view(['POST'])
def object(request):
  
    csv_file = request.FILES['ifile']
    fs = FileSystemStorage()
    filename = fs.save(csv_file.name, csv_file)
    uploaded_file_path = fs.path(filename)
    cap = cv2.VideoCapture(uploaded_file_path)
    while cap.isOpened():
            ret, frame = cap.read()
        
        # Make detections 
            results = model(frame)
        
            cv2.imshow('Yaduvanshi', np.squeeze(results.render()))
        
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
    cap.release()
    return Response (cv2.destroyAllWindows())


@api_view(['GET'])
def object2(request):
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
    
    # Make detections 
        results = model(frame)
    
        cv2.imshow('Yadav', np.squeeze(results.render()))
    
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    return Response (cv2.destroyAllWindows())
