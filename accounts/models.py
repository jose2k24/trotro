from django.db import models
# from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import User
from django.db.models.base import Model

# # Create your models here.
class TrotroAccountManager(models.Model):
    def create_user(self,username, email, firstname ,lastname, password=None):
        if not email:
            raise ValueError("A user must have an Email Address.")

        if not username:
            raise ValueError("A user must have an Username.")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname  = firstname,
            lastname = lastname,
        )

        # setting the password
        user.set_password(password)
        user.save(using=self._db)
        return user

    # creating superuser
    def create_superuser(self,username, email,firstname ,lastname, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            firstname=firstname,
            lastname = lastname,
            password=password,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user



class TrotroAccount(models.Model):
    firstname = models.CharField(max_length=120, blank=False)
    lastname = models.CharField(max_length=120, blank=False)
    username = models.CharField(max_length=120, unique=True, blank=True)
    # name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.username
         
    REQUIRED_FIELDS = ['firstname','lastname','username'] 
     

    # email = None
    # phonenumber = models.CharField(max_length=20)

    # def save_TrotroAccount(self):
    #     self.save()
    # def __str__(self):
    #     return f'{self.post} TrotroAccount'


    # Extras required
    # date_joined = models.DateTimeField(auto_now_add=True)
    # last_login = models.DateTimeField(auto_now_add=True)
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # is_active = models.BooleanField(default=False)
    # is_superadmin = models.BooleanField(default=False)


    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['firstname','lastname','username'] 

    # objects = TrotroAccountManager()

    # def __str__(self):
    #     return self.email

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

    # def has_module_perms(self, add_label):
    #     return True

