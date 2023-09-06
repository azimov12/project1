from django.urls import path
from .views import All, Detail, All2, Detail2, CreateModelView, CreateOfficeView

urlpatterns = [
    path('detail/<int:my_id>', Detail.as_view()),
    path('all/', All.as_view()),
    path('detail2/<int:my_office__id>', Detail2.as_view()),
    path('all2/', All2.as_view()),
    path('create1/', CreateModelView.as_view()),
    path('create2/', CreateOfficeView.as_view()),
]