from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class MyAccountManager(BaseUserManager):
#     def create_user(self, email, username, address, ph_no, password=None):
#         if not email:
#             raise ValueError("users must have an email address")
#         if not username:
#             raise ValueError("Users munt have a username")
#         if not address:
#             raise ValueError("Users must have an address")
#         if not ph_no:
#             raise ValueError("Users must have a phone number")
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             address=address,
#             ph_no=ph_no,
#         )
#         user.set_password(password)
#         user.save(using=self._db)

#         return user

#     def create_superuser(self, email, username, address, ph_no, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#             address=address,
#             ph_no=ph_no,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)

#         return user
class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, address, ph_no, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError("Users munt have a username")
        if not address:
            raise ValueError("Users must have an address")
        if not ph_no:
            raise ValueError("Users must have a phone number")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            address=address,
            ph_no=ph_no,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, address, ph_no, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            address=address,
            ph_no=ph_no,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=60)
    address = models.TextField()
    ph_no = models.CharField(verbose_name="Phone number", max_length=10)
    is_ppty_owner = models.BooleanField(default=False)
    is_tenant = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'address', 'ph_no']

    def __str__(self):
        return self.username

    objects = MyAccountManager()

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

        # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True
