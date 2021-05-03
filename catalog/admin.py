from django.contrib import admin

# Register your models here.

from .models import Role, Image_name, Page_Number, Person, Manumission, Gender, Birth_Place, Death_Place, Age_Listed, Age_Freed, Year_Manumitted, Place_Freed, Monthly_Meeting, Call_Number

admin.site.register(Role)
admin.site.register(Image_name)
admin.site.register(Page_Number)
# admin.site.register(Person)
# admin.site.register(Manumission)
admin.site.register(Gender)
admin.site.register(Birth_Place)
admin.site.register(Death_Place)
admin.site.register(Age_Listed)
admin.site.register(Age_Freed)
admin.site.register(Year_Manumitted)
admin.site.register(Place_Freed)
admin.site.register(Monthly_Meeting)
admin.site.register(Call_Number)

# Define the admin class
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'display_role', 'year_manumitted')
    list_filter = ('gender', 'role', 'age_freed', 'place_freed')
    search_fields = ['first_name','last_name']
# Register the Admin classes for Manumission using the decorator
@admin.register(Manumission)
class ManumissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_person', 'monthly_meeting')
    list_filter = ('call_number', 'monthly_meeting')
