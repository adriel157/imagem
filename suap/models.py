from django.db import models


    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    criacao = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='suap/', null=True, blank=True)
    
    def __str__(self):
        return self.titulo

    
class Comentario(models.Model):
    conteudo = models.TextField()
    autor = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.autor





# Create your models here.
