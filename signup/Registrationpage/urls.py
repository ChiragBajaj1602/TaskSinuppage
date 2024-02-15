from django.urls import path
from . import views
urlpatterns = [
    path('registrationpage',views.homePage.as_view()),
    path('login',views.login.as_view())
]
