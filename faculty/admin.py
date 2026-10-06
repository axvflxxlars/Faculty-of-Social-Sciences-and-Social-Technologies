from django.contrib import admin
from .models import Department, Specialty, Teacher, HomePageContent
from .models import ExchangeProgram

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'head_of_department')
    search_fields = ('name', 'head_of_department')


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'coordinator_name')
    list_filter = ('department',)
    search_fields = ('code', 'name', 'coordinator_name')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'degree', 'department')
    list_filter = ('department', 'position', 'degree')
    search_fields = ('name',)


@admin.register(HomePageContent)
class HomePageContentAdmin(admin.ModelAdmin):
    list_display = ('title',)


    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)

@admin.register(ExchangeProgram)
class ExchangeProgramAdmin(admin.ModelAdmin):
    list_display = ('university', 'languages', 'places', 'deadline')
