from django.contrib import admin

# Register your models here.
from backend.models import CoreUser, Badge, Exercise, Quest

admin.site.register(CoreUser)
admin.site.register(Badge)
admin.site.register(Exercise)
admin.site.register(Quest)
# admin.site.register(Doctor)
