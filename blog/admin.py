from django.contrib import admin
from .models import *
from django.db import models
# Register your models here.

class post(admin.ModelAdmin): # bu alanın admin sayfasında otomatik olarak girmes için admin model deyip admine register ettik.
    prepopulated_fields={'slug':('title',)}


admin.site.register(CreatePost,post)