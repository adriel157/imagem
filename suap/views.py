from django.shortcuts import render
from .models import Comentario,Post


def index(request):
    comentarios = Comentario.objects.all() # Select do django
    posts  =  Post.objects.all()
    contexto = {
        'comentarios': comentarios,
        'posts': posts,
    }
    return render(request, 'suap/index.html',contexto)


def sobre(request):
    return render(request, 'suap/sobre.html')

 


# Create your views here.
