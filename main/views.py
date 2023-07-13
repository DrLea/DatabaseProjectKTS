from rest_framework import generics
from .permissions import IsOwnerOrAdmin, IsAdminOrReadOnly
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView


#TOKEN
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer


class CustomTokenVerifyView(TokenVerifyView):
    serializer_class = CustomTokenVerifySerializer


#USER
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            # If the user is a superuser, return the full queryset
            return super().get_queryset()
        else:
            # If the user is not a superuser, return an empty queryset
            return User.objects.none()


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Allow only staff and the user who created the instance
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            # Allow read-only access for unauthenticated users
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()



#EVENT
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Allow only staff and the user who created the instance
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            # Allow read-only access for unauthenticated users
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

class EventListOfUserView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(user = self.kwargs['user_id'])





#BOOK
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Allow only staff and the user who created the instance
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            # Allow read-only access for unauthenticated users
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

class BookListOfUserView(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.filter(user = self.kwargs['user_id'])


#VIDEO
class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VideoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Allow only staff and the user who created the instance
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            # Allow read-only access for unauthenticated users
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

class VideoListOfUserView(generics.ListAPIView):
    serializer_class = VideoSerializer

    def get_queryset(self):
        return Video.objects.filter(user = self.kwargs['user_id'])

#FILE
class FileListCreateView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Allow only staff and the user who created the instance
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            # Allow read-only access for unauthenticated users
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

class FileListOfUserView(generics.ListAPIView):
    serializer_class = FileSerializer

    def get_queryset(self):
        return File.objects.filter(user = self.kwargs['user_id'])

#PODCAST
class PodcastListCreateView(generics.ListCreateAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PodcastRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Allow only staff and the user who created the instance
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            # Allow read-only access for unauthenticated users
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

class PodcastListOfUserView(generics.ListAPIView):
    serializer_class = PodcastSerializer

    def get_queryset(self):
        return Podcast.objects.filter(user = self.kwargs['user_id'])


#COMMENT
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            # Allow only staff and the user who created the instance
            self.permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
        else:
            # Allow read-only access for unauthenticated users
            self.permission_classes = [IsAuthenticatedOrReadOnly]
        return super().get_permissions()

class CommentListOfUserView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(user_id = self.kwargs['user_id'])

class CommentListByContentIDView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get_queryset(self):
        content = Content.objects.get(id = self.kwargs['content_id'])
        return content.comment_set.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)