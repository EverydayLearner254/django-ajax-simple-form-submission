from django.urls import path
from .views import index, save, modal
app_name = 'form'

urlpatterns = [
    path('', index, name='index'),
    path('modal', modal, name='modal'),
    path('save/', save, name='save'),
]