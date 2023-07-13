
from django.contrib import admin
from django.urls import path
from obj2app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vedio/', views.object),
    path('vediolive/', views.object2),
    #path('vediopost/', views.DetectCreate.as_view()),
]
