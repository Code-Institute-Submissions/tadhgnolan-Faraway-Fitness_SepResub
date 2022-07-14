from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.memberships, name='memberships'),
    path('add/', views.add_membership, name='add_membership'),
    path(
        'edit/<int:membership_id>/',
        views.edit_membership, name='edit_membership'),
    path(
        'delete/<int:membership_id>/',
        views.delete_membership, name='delete_membership'),
]
