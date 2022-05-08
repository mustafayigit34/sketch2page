from django.urls import path

from main.views import upload_view, result_view

urlpatterns = [
    path('', upload_view, name='home'),
    path('result', result_view, name='result')
]
