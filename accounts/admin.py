from django.contrib import admin

from accounts.models import Profile, Country



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']


class CountryAdmin(admin.ModelAdmin):
    list_display = ['name', 'abbreviation', 'is_active']


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Country, CountryAdmin)
