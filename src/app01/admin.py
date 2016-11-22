from django.contrib import admin

from . import models

# Register your models here.

class BBS_admin(admin.ModelAdmin):
    list_display=('title', 'summary', 'author', 'signature', 'created_at', 'update_at')
    list_filter=('created_at', 'update_at')
    search_fields = ('title', 'author__user__username')
    
    def signature(self, obj):
        return obj.author.signature
    
    #signature.shortDescription = "sing"

admin.site.register(models.BBS, BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
admin.site.register(models.Comments)