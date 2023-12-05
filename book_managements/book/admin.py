from django.contrib import admin
from .models import book_management,patron_management,book_borroewing
admin.site.register(book_management)
admin.site.register(patron_management)
admin.site.register(book_borroewing)

# # Register your models here.
