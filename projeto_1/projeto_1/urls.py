from django.urls import path
from hello.views import hello_word

urlpatterns = [
    path('',hello_word),
]
