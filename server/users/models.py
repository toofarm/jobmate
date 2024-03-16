from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import validate_email


class CustomUserManager(UserManager):

    def _get_email(self, email: str):
        validate_email(email)
        return self.normalize_email(email)

    def _create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        commit: bool,
        is_staff: bool = False,
        is_superuser: bool = False,
    ):

        email = self._get_email(email)

        user = User(
            email=email,
            username=email,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
        )
        user.set_password(password)

        if commit:
            user.save()

        return user

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        commit: bool = True,
    ):
        return self._create_user(
            email,
            password,
            first_name,
            last_name,
            is_staff=True,
            is_superuser=True,
            commit=commit,
        )

    def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        commit: bool = True,
    ):
        return self._create_user(email, password, first_name, last_name, commit=commit)


# Create your models here.
class User(AbstractUser):

    email = models.EmailField(unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=150, blank=False, null=False)
    target_job_title = models.CharField(max_length=150, blank=True, null=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    pass
