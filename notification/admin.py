from django.contrib import admin
from .models import NotificationPreference, NotificationLog

@admin.register(NotificationPreference)
class NotificationPreferenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'email_enabled', 'minutes_before', 'created_at', 'updated_at')
    list_filter = ('email_enabled',)
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(NotificationLog)
class NotificationLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'match', 'notification_type', 'status', 'sent_at')
    list_filter = ('notification_type', 'status')
    search_fields = ('user__username', 'user__email', 'match__id', 'match__player1__name', 'match__player2__name')
    readonly_fields = ('sent_at',)

