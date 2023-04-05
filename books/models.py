from django.db import models
from django.urls import reverse

# Create your models here.
class Books(models.Model):
    title=models.CharField(max_length=255)
    content = models.TextField(blank=True)
    publication_date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(blank=True, null=True, default='1.png')
    publisher = models.ForeignKey('Publisher', on_delete=models.SET_NULL, null=True)
    author=models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)

    def __str__(self):   
        return self.title
    
    class Meta:
         verbose_name_plural = "Books"
         ordering = ['title', 'publication_date']

    def get_absolute_url(self):
            return reverse('book', kwargs={'book_id': self.pk})
    
class Publisher(models.Model):
     name = models.CharField(max_length=100, db_index=True)
     address = models.CharField(max_length=100, null=True)

     def __str__(self):
        return self.name
     
     
class Author(models.Model):
     name = models.CharField(max_length=100, db_index=True, null=True)
     photo = models.ImageField(blank=True, null=True, default='1.png')
     email = models.EmailField(max_length=50, null=True)

     def __str__(self):
        return self.name