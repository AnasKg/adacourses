from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('users/', views.users_list, name='users_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
    path('posts/create/', views.create_post, name = 'create_post'),
    path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),

    path('products/', views.see_product, name='product_list'),
    path('products/create/', views.create_product, name='create_product')
]
