from django.urls import path

from . import views

urlpatterns = [
    path("stories", views.story, name="stories"),
    path("posts", views.posts, name="posts"),
    path("categories", views.categories, name="categories"),
    path("categories/<int:category_id>", views.category, name="category"),
    path("products", views.products, name="products"),
    path("products/<int:product_id>", views.product, name="product"),
    path("users", views.users, name="users"),
    path("users/<int:user_id>", views.user, name="user"),

]