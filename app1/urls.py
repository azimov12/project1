from django.urls import path
from .views import all, detail

urlpatterns = [
    path('all/', all),
    path('detail/<int:my_id>', detail)
]