from django.urls import path
from django.urls import re_path as url 

from lib_app.views import LibraryView

urlpatterns = [
    path('books/',LibraryView.as_view()),
    path('books/<int:pk>/',LibraryView.as_view()),


]
