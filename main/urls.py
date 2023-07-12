from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('users/', UserListCreateView.as_view(), name='user_list_create'),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
    path('content/events', EventListCreateView.as_view(), name='event_list_create'),
    path('content/event/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event_retrieve_update_destroy'),
    path('content/events/of_user/<int:user_id>/', EventListOfUserView.as_view(), name='events_of_user'),
    path('content/books', BookListCreateView.as_view(), name='book_list_create'),
    path('content/book/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book_retrieve_update_destroy'),
    path('content/books/of_user/<int:user_id>/', BookListOfUserView.as_view(), name='books_of_user'),
    path('content/videos', VideoListCreateView.as_view(), name='video_list_create'),
    path('content/video/<int:pk>/', VideoRetrieveUpdateDestroyView.as_view(), name='video_retrieve_update_destroy'),
    path('content/video/of_user/<int:user_id>/', VideoListOfUserView.as_view(), name='videos_of_user'),
    path('content/files', FileListCreateView.as_view(), name='file_list_create'),
    path('content/file/<int:pk>/', FileRetrieveUpdateDestroyView.as_view(), name='file_retrieve_update_destroy'),
    path('content/files/of_user/<int:user_id>/', FileListOfUserView.as_view(), name='files_of_user'),
    path('content/podcasts', PodcastListCreateView.as_view(), name='podcast_list_create'),
    path('content/podcast/<int:pk>/', PodcastRetrieveUpdateDestroyView.as_view(), name='podcast_retrieve_update_destroy'),
    path('content/podcast/of_user/<int:user_id>/', PodcastListOfUserView.as_view(), name='podcasts_of_user'),
    path('comments', CommentListCreateView.as_view(), name='comment_list_create'),
    path('comment/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment_retrieve_update_destroy'),
    path('comment/for_content/<int:content_id>/', CommentListByContentIDView.as_view(), name='comment_list_by_content_id'),
    path('comment/of_user/<int:user_id>/', CommentListOfUserView.as_view(), name='comments_of_user'),
]