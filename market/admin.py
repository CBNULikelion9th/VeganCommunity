from django.contrib import admin
from .models import Market_Post

@admin.register(Market_Post)
class PostAdmin(admin.ModelAdmin):
    pass

