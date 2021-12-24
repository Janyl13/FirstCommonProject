
from django.contrib import admin

from .models import *


class ImageInLineAdmin(admin.TabularInline):
    model = Image
    fields = ('image')
    max_num = 5


admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Destination)
admin.site.register(Category)
admin.site.register(Image)


