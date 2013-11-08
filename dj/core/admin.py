from core.models import Local, Comment
from django.contrib import admin

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class LocalAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name','user']}),
        ('Data', {'fields': ['cord','addr'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('name', 'addr')
    list_filter = ('name', 'addr')
    search_fields = ('name',)

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Local, LocalAdmin)
#admin.site.register(Comment, CommentAdmin)

