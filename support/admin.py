'''
File: admin.py
Project: edutours.com.ng
File Created: Wednesday, 26th February 2020 7:12:13 pm
Author: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Last Modified: Tuesday, 9th June 2020 1:57:40 pm
Modified By: Temitayo Bodunrin (temitayo@camelcase.co)
-----
Copyright 2020, CamelCase Technologies Ltd
'''
from django.contrib import admin
from .models import SiteSetting, EmailTemplate


class BaseAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('created_at', 'name')
    list_filter = ['name', 'created_at']
    search_fields = ['name']
    list_display_links = ['name', 'created_at']
    save_as = True


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'value')
    search_fields = ('name', 'value')
    list_editable = ('name', 'value')
    save_as = True


@admin.register(EmailTemplate)
class EmailTemplateAdmin(BaseAdmin):
    pass
