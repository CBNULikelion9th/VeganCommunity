from django.contrib import admin
from .models import Post, Market_Post, Market_Comment
from signup.models import User, UserManager


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_superuser')
    fields = ('__all__',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('store_name', 'location')
    fields = ('__all__',)

class MarketPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer')
    fields = ('__all__',)

class MarketCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment')
    fields = ('__all__',)

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Market_Post, MarketPostAdmin)
admin.site.register(Market_Comment, MarketCommentAdmin)