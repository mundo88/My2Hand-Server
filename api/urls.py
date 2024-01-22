from django.urls import path

from . import views

urlpatterns = [
    path("stories", views.story, name="stories"),
    path("posts", views.posts, name="posts"),
    path("categories", views.categories, name="categories"),
    path("products", views.products, name="products"),
    path("users", views.users, name="users"),
]