#DJANGO IPORT
from django.contrib import admin
#APP IMPORT
from .models import Post

# Register your models here.
#CONSTRUCCION BASICA
#admin.site.register(Post)

#CONSTRUCCION COSTUMISADA
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #COSTUMIZACION INICIAL
    list_display = ('title','slug','author','publish','status')
    #COSTUMIZACION AVANZADA
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')



from .models import Post, Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')