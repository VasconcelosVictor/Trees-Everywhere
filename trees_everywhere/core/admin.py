from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Profile, Account, Plant, PlantedTree

class ProfileInline(admin.StackedInline):
   model = Profile
   can_delete = False
 

class UserAdmin(admin.ModelAdmin):
   inlines = (ProfileInline,)
   list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

class AccountAdmin(admin.ModelAdmin):
   list_display = ('name', 'active' )
   list_filter = ('active',)
   search_fields = ('name',)

class PlantedTreeInline(admin.TabularInline):
   model = PlantedTree
   extra = 0

class PlantAdmin(admin.ModelAdmin):
   inlines = (PlantedTreeInline,)
   list_display = ('name', 'scientific_name')
   search_fields = ('name', 'scientific_name')

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Plant, PlantAdmin)
