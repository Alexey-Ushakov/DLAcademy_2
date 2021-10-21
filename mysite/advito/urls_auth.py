from django.urls import path


from .views_auth import (
    LoginView, logout_view, ProfileView, EditProfileView
)


urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
    path('profile/<int:user_id>', ProfileView.as_view(), name='profile'),
    path('profile/<int:user_id>/edit', EditProfileView.as_view(), name='edit_profile')
]