
from django.urls import path
from polls.views import funkcja_widoku, hello_name, index

urlpatterns = [
    path("", index, name="index"),
    path('hello/', funkcja_widoku),
    path('hello/<name>', hello_name),
]