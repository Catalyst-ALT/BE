from django.contrib import admin
from .models import User, Poem, Prompt
# Register your models here.

admin.site.register(User)
admin.site.register(Poem)
admin.site.register(Prompt)
