from django.urls import path


from .views_auth import (
    LoginView
)

app_name ='advito'

urlpatterns = [
    path('login', LoginView.as_view(), name="login")
]