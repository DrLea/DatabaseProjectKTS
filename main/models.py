from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager, Permission, Group
from django.utils.timezone import now

from django.core.validators import MinValueValidator
from django.db import models


# USER
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, nickname, age, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError('Password is not provided')

        user = self.model(
            email = self.normalize_email(email),
            nickname = nickname,
            age = age,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, nickname, age, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email, password, nickname, age,  **extra_fields)

    def create_superuser(self, email, password, nickname, age, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email, password, nickname, age, **extra_fields)




class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    image = models.ImageField(upload_to=".images/avatars/", null=True, blank=True)
    age = models.IntegerField(validators=[MinValueValidator(5)])
    description = models.TextField(blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname', 'age',]

    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to',
        related_name='custom_user_set'  # Custom related_name to resolve the clash
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='The permissions this user has',
        related_name='custom_user_set'  # Custom related_name to resolve the clash
    )



    def __str__(self) -> str:
        return f'{self.nickname} - {self.age}'



class Interest(models.Model):
    interested_in = models.ManyToManyField(User, related_name='interests')
    name = models.CharField(max_length=20, unique=True, blank=False)


# CONTENT
class Content(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    image = models.ImageField(upload_to='.images/cover_pages/', null=True, blank=True)
    tag = models.TextField(max_length=20, null=True)
    isApproved = models.BooleanField(default=False)
    date = models.DateTimeField(default=now)



    def __str__(self) -> str:
        return f'{self.name} - {self.isApproved}'
    

class _Content(models.Model):
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def __str__(self) -> str:
        return f'{self.content_id}'
    
    class Meta:
        abstract = True
    

class Event(_Content):
    location = models.URLField()


class Book(_Content):
    source = models.FileField(upload_to=".files/books/")


class Video(_Content):
    source = models.FileField(upload_to=".files/videos/")


class File(_Content):
    file = models.FileField(upload_to=".files/files/")


class Podcast(_Content):
    file = models.FileField(upload_to=".files/podcasts/")


# COMMENT
class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    text = models.TextField()