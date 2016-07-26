from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    """customize the model admin"""
    list_display = ["title", "timestamp", "updated"]
    # list_display_links = ["updated"]
    list_filter = ["title", "updated"]
    search_fields = ["title", "content"]
    # list_editable = ["title"]
    class Meta:
        model = Post



# register our model to admin dasboard
admin.site.register(Post, PostAdmin)
