from django.contrib import admin
from tracker.models import curr_balance, track_history
# Register your models here.

admin.site.register(curr_balance)

class TrackHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance', 'amount', 'expense_type', 'description', 'created_at', 'updated_at')
    list_filter = ('expense_type', 'created_at')
    search_fields = ('description',)


admin.site.register(track_history, TrackHistoryAdmin)
