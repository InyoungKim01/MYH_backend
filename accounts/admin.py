from django.contrib.auth import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

#회원가입을 한 유저정보를 바탕으로 프로필을 만듦 -> 프로필 수정이 가능함
class ProfileInline(admin.StackedInline): # 유저 밑에 프로필을 붙여서 보여주려고 이를 상속받음
    model = Profile
    con_delete = False                    
    verbose_name_plural = "profile"

class CustomUserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# 기존의 User의 등록을 취소했다가 User와 ProfileInline을 붙임.
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)





from django.contrib import admin
#
# # Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import User
#
admin.site.register(User)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "profile"


class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

#
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
