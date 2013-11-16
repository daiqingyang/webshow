from django.contrib import admin
from home.models import  *
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('username','className','date','time')
    list_filter = ('username','className',"date","username")
class AddClassAdmin(admin.ModelAdmin):
    list_display = ('className','invate_key','canRegister')
class StudentAdmin(admin.ModelAdmin):
    list_display = ('username','password','className','invate_key')
admin.site.register(AddClass,AddClassAdmin)
admin.site.register(Attendence,AttendenceAdmin)
admin.site.register(Student,StudentAdmin)
