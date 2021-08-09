from django.contrib import admin
from signup.models import User
from blog.models import Report, Add
from market.models import Market_Comment


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin', 'is_superuser')
    fields = ('__all__',)

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_title', 'report_content')
    fields = ('__all__',)

class AddAdmin(admin.ModelAdmin):
    list_display = ('add_title', 'add_content')
    fields = ('__all__',)

class MarketCommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment')
    fields = ('__all__',)

admin.site.register(User, UserAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(Add, AddAdmin)
admin.site.register(Market_Comment, MarketCommentAdmin)