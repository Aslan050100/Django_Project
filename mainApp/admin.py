from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["id","name","email"]
    search_fields = ["name"]
    list_filter = ["name"]
    class Meta:
        model = Subscriber


admin.site.register(Subscriber,SubscriberAdmin)