from django.contrib import admin
from .models import Post, Author , Carousel , Project , Services , Video ,Contact
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','image','auther','views' , 'created_at', 'updated_at')
    search_fields = ('title', 'auther__name')
    exclude = ['slug','views']

class CarouselAdmin(admin.ModelAdmin):
    list_display = ('position','title','image')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','slug','image','developer','views' , 'created_at', 'updated_at')
    search_fields = ('title', 'developer')
    exclude = ['slug','views']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title','slug','image','views' , 'created_at', 'updated_at')
    search_fields = ('title', 'views')
    exclude = ['slug','views']

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title','video_link', 'created_at', 'updated_at')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','number','message', 'created_at', 'updated_at')
    exclude=['name','email','number','message', 'created_at', 'updated_at']

admin.site.register(Post, PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Contact, ContactAdmin)
# Register your models here.
