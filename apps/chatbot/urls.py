from django.urls import path

from .views import index


app_name = "chatbot"

urlpatterns = [
    path('', index.index, name='index'),
]