from django.contrib import admin
from .models import Post,Comentario
from django.utils.html import format_html



class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo','conteudo','criacao')
admin.site.register(Post ,PostAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('conteudo','autor','post')
admin.site.register(Comentario ,ComentarioAdmin)



# Register your models here.
