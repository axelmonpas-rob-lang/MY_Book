from django.db import models

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=250)


    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.title
    
class Book(models.Model):
        
        title = models.CharField(max_length=250)
        author = models.CharField(max_length=250)
        image = models.ImageField(upload_to='books/', blank=True, null=True)
        created_at =models.DateTimeField(auto_now_add=True)
        update_at = models.DateTimeField(auto_now=True)