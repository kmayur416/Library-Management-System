from django.contrib import admin
from .models import *


class Bookadmin(admin.ModelAdmin):
    list_display = ["book_id", "book_name", "author_name", "category", "stock_quantity", "created", "modified", "language"]
    list_filter = ["book_name","book_id"]
    ordering = ('-created',)


admin.site.register(Book,Bookadmin)