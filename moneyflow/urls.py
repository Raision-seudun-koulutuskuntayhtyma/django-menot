from django.urls import path

from . import views

urlpatterns = [
    path("", views.frontpage, name="index"),
    path("tilit/", views.AccountsList.as_view(), name="accounts"),
    path("dokumentit/", views.documents, name="documents"),
]
