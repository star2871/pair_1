from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk_>", views.detail, name="detail"),
    path("update/<int:pk_>", views.update, name="update"),
    path("delete/<int:pk>", views.delete, name="delete"),
    path("create/", views.create, name="create"),
    path("new/", views.new, name="new"),
    path("edit/<int:pk_>", views.edit, name="edit"),
]
