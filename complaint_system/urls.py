from atexit import register
from django.contrib import admin
from django.urls import path
from complaint_system import views

urlpatterns = [
    path("", views.login, name="login"),
    path("registration", views.registration, name="registration"),
    path("ticket", views.complaint_ticket, name="ticket"),
    path("admin_page", views.admin_page, name="admin"),
    path("user_registration", views.user_registration, name="user registration"),
    path("admin_registration", views.admin_registration, name="admin registration"),
    path("user_login", views.user_login, name="user login"),
    path("admin_login", views.admin_login, name="admin login"),
]