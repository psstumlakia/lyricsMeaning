from django.contrib import admin
from accounts.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_info', 'nickname', 'interests', )

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-nickname')
        return queryset

    user_info.short_description = 'Info'    # Override user info name again


# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)