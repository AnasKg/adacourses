from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # path('posts/', views.post_list, name='post_list'),
    path('posts/', views.PostListView.as_view(), name='post_list'),

    # path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/<int:post_id>/', views.PostDetailView.as_view(), name='post_detail'),
    path('posts/<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    path('users/', views.users_list, name='users_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),

    path('posts/create/', views.PostCreateView.as_view(), name = 'create_post'),
    # path('posts/create/', views.PostView.as_view(), name = 'create_post'),
    
    path('posts/<int:post_id>/edit/', views.PostUpdateView.as_view(), name='edit_post'),

    path('products/', views.see_product, name='product_list'),
    path('products/create/', views.create_product, name='create_product'),

    path('posts/<int:post_id>/comments/<int:comment_id>/', views.edit_comment, name='edit_comment'),
    path('post/<int:post_id>/comment/', views.CommentCreateView.as_view(), name='create_comment'),
]
