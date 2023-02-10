from django.contrib import admin
from .models import *
#from .models import Literature
# Register your models here.

class LiteratureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Literature, LiteratureAdmin)

class ArtworkAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Artwork, ArtworkAdmin)

class VisAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('video',)}

admin.site.register(Vis, VisAdmin)