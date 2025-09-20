from django.views.generic import TemplateView
from django.urls import path


app_name = "chatbot"

urlpatterns = [
    path('', TemplateView.as_view(template_name='chatbot/index.html'), name='index'),
]