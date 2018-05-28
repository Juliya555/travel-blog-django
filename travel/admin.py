from django.contrib import admin
from .models import *


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 0


class PlaceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Place._meta.fields]
    inlines = [PlaceImageInline]

    class Meta:
        model = Place


admin.site.register(Place, PlaceAdmin)


class PlaceImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PlaceImage._meta.fields]

    class Meta:
        model = PlaceImage


admin.site.register(PlaceImage, PlaceImageAdmin)


class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ["name"]
    search_fields = ["name", "email"]

    fields = ["email"]


admin.site.register(Subscriber, SubscriberAdmin)
