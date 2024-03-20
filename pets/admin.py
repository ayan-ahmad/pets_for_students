from django.contrib import admin
from pets.models import Student, Cat

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'num_cats')

class CatAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

admin.site.register(Cat, CatAdmin)
admin.site.register(Student, StudentAdmin)
