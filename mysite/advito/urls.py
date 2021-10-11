from django.urls import path
from .views import index, announcement, post_detail,post_create, post_edit, post_delete, category, choise_category

urlpatterns = [
    path('', index, name="index"),
    path('announcement/', announcement, name="announcement"),
    path('announcement/<int:post_id>/', post_detail, name="post_detail"),
    path('announcement/create/', post_create, name="post_create"),
    path('announcement/<int:post_id>/edit', post_edit, name="post_edit"),
    path('announcement/<int:post_id>/delete', post_delete, name="post_delete"),
    path('category/', category, name="category"),
    path('category/<int:category_id>', choise_category, name="category")
]

