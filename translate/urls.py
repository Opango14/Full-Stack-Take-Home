from django.urls import path
from .views import index, translate_text_api

app_name = 'translate'

urlpatterns = [
    path('', index, name='index'),
    path('api/v1/translate-text', translate_text_api, name='translate_api')
]
