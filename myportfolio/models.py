from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField( max_length=254)
    name =models.CharField(max_length= 120)
    subject = models.TextField()
    Message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name