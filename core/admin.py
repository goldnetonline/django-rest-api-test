

from datetime import datetime
from django.contrib import admin
from django.utils.translation import gettext_lazy as _


# Register your models here.
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User


tz = str(datetime.now().timestamp()).split(".")[0]


def renderImage(url):
    return format_html("<img src='{}' width='100' />".format(url))


def logoDisplay(obj):
    if not obj.logo:
        return ''
    logoPath = obj.logo.url
    return renderImage(logoPath)


logoDisplay.short_description = 'Logo'


def imageDisplay(obj):
    if not obj.image:
        return ''
    image = obj.image.thumb.url if obj.image.thumb else obj.image.url
    return renderImage(image)


imageDisplay.short_description = 'Avatar'


def statusBadge(obj):
    status = obj.d_status or obj.status
    if not status:
        return ""

    return format_html('<span class="badge {} badge-caps-sm">{}</span>'.format(
        "badge-danger" if status.lower() in 'pending rejected' else 'badge-success',
        status
    ))


statusBadge.short_description = 'Status'


@admin.register(User)
class UserAdminOverride(UserAdmin):
    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Avatar'), {'fields': ('avatar',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name',
                    'is_staff')
    list_filter = ('is_staff',
                   'is_superuser', 'is_active', 'groups')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created_at',)
    filter_horizontal = ('groups', 'user_permissions',)


class BaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('created_at', 'name')
    list_filter = ['name', 'created_at']
    search_fields = ['name']
    list_display_links = ['name', 'created_at']

    # Enable this temprarily to be able to make copies
    save_as = True
