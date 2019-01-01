from django.contrib import admin
from django.urls import path
from firstapp import views
 
urlpatterns = [
    path('', views.index),
    path(r'admin/', admin.site.urls),
	
	
	]

