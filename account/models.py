from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from tag.models import Tag
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = True
        user.staff = True
        user.developer = True
        user.company = True
        user.save(using=self._db)
        return user

    def create_company_user(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = False
        user.staff = False
        user.company = True
        user.developer = False
        user.save(using=self._db)
        return user

    def create_developer_user(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.admin = False
        user.staff = False
        user.company = False
        user.developer = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_(
            'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
        null=True,
    )
    is_activated = models.BooleanField(default=True)

    email = models.EmailField(max_length=255, unique=True)

    # Developer fields
    gender = models.CharField(
        choices=[('male', 'male'), ('female', 'female')], max_length=6, default='male', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    applied_job = models.ForeignKey(
        'job.Job',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    allow_mail_notification = models.BooleanField(default=True, null=True)

    # Company fields
    address = models.CharField(max_length=300, null=True, blank=True)
    history = models.TextField(null=True, blank=True)

    # User type fields
    company = models.BooleanField(default=False)
    developer = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        "Is the user a member of staff?"
        return self.admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.admin

    @property
    def is_company(self):
        "Is the user a admin member?"
        return self.company

    @property
    def is_developer(self):
        "Is the user a admin member?"
        return self.developer

    objects = UserManager()
