from django.contrib import admin

from .models import Person

# Register your models here.
@admin.register(Person)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','DOB','phone']