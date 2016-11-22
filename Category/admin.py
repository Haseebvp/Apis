from django.contrib import admin

# Register your models here.
from Category.models import *

admin.site.register(MainCategoryTable)
admin.site.register(CategoryTable)
admin.site.register(SubCategoryTable)