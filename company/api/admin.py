from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

class EmpAdmin(admin.ModelAdmin):
    list_display=('name','address','phone')
    list_filter=('company',)
    


admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmpAdmin)