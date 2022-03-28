from django.urls import path
from . import views
from .views import *
urlpatterns = [
    path('',postListView.as_view(),name='blog-home'),
    path('post/<int:pk>/',postDetailView.as_view(),name='post-detail'),
    path('post/new/',postCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/',postUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',postDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/comment/',postCommentCreateView.as_view(),name='post-comment'),
    path('placements/',views.placed,name='placements'),
    path('about/',views.about,name='blog-about')
]