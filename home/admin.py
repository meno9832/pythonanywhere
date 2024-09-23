from django.contrib import admin
from .models import main_notice, Post, banner, dday,gallery
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

@admin.register(main_notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('notice_text', 'cover_img_url')


admin.site.register(Post, PostAdmin)
admin.site.register(banner)
admin.site.register(dday)
admin.site.register(gallery)