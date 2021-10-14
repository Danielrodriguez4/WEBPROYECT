from django.urls import path
from project.views import Index

app_label = 'project'

urlpatterns = [
    path('', Index.as_view(), name='home')
] 
