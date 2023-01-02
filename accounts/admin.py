from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from profiles.models import TrotroAccount, UserProfile
# from django.utils.html import format_html

# # Register your models here.
admin.site.register(TrotroAccount)
admin.site.register(UserProfile)

