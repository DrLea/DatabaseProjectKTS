from rest_framework import generics
from .models import *
from .permissions import IsOwnerOrAdmin, IsAdminOrReadOnly
from .serializers import *
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



#USER
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminOrReadOnly,)



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

class CommentListByContentIDView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


    def get_queryset(self):
        content = Content.objects.get(id = self.kwargs['content_id'])
        return content.comment_set.all()