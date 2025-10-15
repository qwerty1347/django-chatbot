from django.views.generic import TemplateView
from django.urls import path

from config import settings

from .views import index


app_name = "chatbot"

urlpatterns = [
    path('', TemplateView.as_view(
            template_name='chatbot/index.html',
            extra_context={'CHATBOT_API_URL': settings.env('CHATBOT_API_URL')}
        ),
        name='index'
    ),
    path('api', index.index, name="api"),
]