from django.contrib import admin
from .models import Student
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['prenom','nom','domaine_etude']
    search_fields=['prenom','nom','domaine_etude']
    list_filter=['gpa']