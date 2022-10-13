from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin
from portal.models import *

# Register your models here.
admin.site.site_header = "CTAC PastCare admin"
admin.site.site_title = "CTAC PastCare admin site"
admin.site.index_title = "CTAC PastCare admin"


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'phone', 'last_login', 'date_joined')
    list_display_links = ('email', 'username', 'phone')
    readonly_fields = ('last_login', 'date_joined')
    # am ordering  date joined by descending order
    ordering = ('-date_joined',)
    # Used so the other required fields such as groups is disabled
    filter_horizontal = ()
    list_filter = ()
    # Used to make password read only
    fieldsets = ()


#
@admin.register(DBUser)
class DBUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'chapel', 'group']
    fields = ['title', 'name', 'email', 'chapel', 'group']
    search_fields = ['name']


@admin.register(Chapels)
class ChapelsAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    fields = ['name']
    search_fields = ['name']


@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'group', ]
    list_filter = ['group', ]
    search_fields = ['phone_number', 'last_name', 'first_name']


@admin.register(RoleUser)
class RoleUserAdmin(admin.ModelAdmin):
    list_display = ['role', 'user']


@admin.register(Attendances)
class AttendancesAdmin(admin.ModelAdmin):
    list_display = ['service_date', 'is_present']
    search_fields = ['service_date', 'member']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(AttendanceSummaries)
class AttendanceSummariesAdmin(admin.ModelAdmin):
    list_display = ['weekday', 'attendance_date', 'group', 'total_present']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
