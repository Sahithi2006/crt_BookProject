from django .urls import path,include
from django.urls import path
from .views import home_page,profile_page,contact_page,marks_page,add_user
urlpatterns = [
    path("home/",home_page),
    path("profile/",profile_page),
    path("contact/",contact_page),
    path("marks/", marks_page),
    path("user_form/",add_user)
]