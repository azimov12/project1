from django.urls import path
from .views import all, detail, all2, detail2

urlpatterns = [
    path('detail/<int:noutbook_id>', detail),
    path('all/', all),
    path('detail2/<int:keyboard_id>', detail2),
    path('all2/', all2),
]