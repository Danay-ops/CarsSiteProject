from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cars, Categories,UploadF,AddContact
# Register your models here.




class CarsAdmin(admin.ModelAdmin):
    list_display = ('id','title','post_photo', 'is_published','time_create','cat')
    list_display_links = ('id','title')
    search_fields = ['title','cat__name']
    readonly_fields = ['post_photo']
    save_on_top = True

    def post_photo(self, cars: Cars):
        if cars.photo:
            return mark_safe(f"<img src='{cars.photo.url}' width=100>")
        else:
            return 'Без фото'

admin.site.register(Cars,CarsAdmin)
admin.site.register(Categories)
admin.site.register(UploadF)
admin.site.register(AddContact)