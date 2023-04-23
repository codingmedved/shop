from django.contrib import admin
from .models import *


class SubscriberAdmin(admin.ModelAdmin):
    # list_display = ['name', 'email']
    list_display = [field.name for field in Subscribers._meta.fields]
    # list_filter = ['name']
    search_fields = ['name']

    # fields = ['name']
    # exclude = ['name']

    class Meta:
        model = Subscribers


admin.site.register(Subscribers, SubscriberAdmin)
