from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import *

admin.site.register(EventCategory)
admin.site.register(EventCategoryUser)
admin.site.register(Event, MapAdmin)
admin.site.register(EventMember)
admin.site.register(UserCoin)
