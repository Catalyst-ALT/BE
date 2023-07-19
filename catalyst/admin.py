from django.contrib import admin
from .models import User, Write, VisualArt, Note
# Register your models here.

admin.site.register(User)
admin.site.register(Write)
admin.site.register(VisualArt)
admin.site.register(Note)
