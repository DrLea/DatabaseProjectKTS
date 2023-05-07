from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
    path('content/events', EventListCreateView.as_view(), name='event_list_create'),
    path('content/event/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event_retrieve_update_destroy'),
    path('content/books', BookListCreateView.as_view(), name='book_list_create'),
    path('content/book/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book_retrieve_update_destroy'),
    path('content/videos', VideoListCreateView.as_view(), name='video_list_create'),
    path('content/video/<int:pk>/', VideoRetrieveUpdateDestroyView.as_view(), name='video_retrieve_update_destroy'),
    path('content/files', FileListCreateView.as_view(), name='file_list_create'),
    path('content/file/<int:pk>/', FileRetrieveUpdateDestroyView.as_view(), name='file_retrieve_update_destroy'),
    path('content/podcasts', PodcastListCreateView.as_view(), name='podcast_list_create'),
    path('content/podcast/<int:pk>/', PodcastRetrieveUpdateDestroyView.as_view(), name='podcast_retrieve_update_destroy'),
    path('comments', CommentListCreateView.as_view(), name='comment_list_create'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_retrieve_update_destroy'),
]