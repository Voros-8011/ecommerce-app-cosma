from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from form.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'is_staff', 'is_active', 'age','gender','phone_num','adress','role']
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ('age','gender','phone_num','adress','role')}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ('age','gender','phone_num','adress','role')}),)

admin.site.register(CustomUser, CustomUserAdmin)