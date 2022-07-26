from django.contrib import admin
from .models import Quiz, UserProfile, Question

# Register your models here.
admin.site.register(Quiz)
admin.site.register(UserProfile)
admin.site.register(Question)
