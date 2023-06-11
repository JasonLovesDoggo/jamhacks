from django.contrib import admin

# Register your models here.
from .models import CoreUser, Badge, Exercise, Quest, Doctor

admin.site.register(CoreUser)
admin.site.register(Badge)
admin.site.register(Exercise)
admin.site.register(Quest)
# admin.site.register(Doctor)
