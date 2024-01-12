from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("html_page/", html_page),
    path("page2/", page2),
    path("get_form_data/", get_form_data_and_save, name='get_form_data'),
]